from collections.abc import Sequence
from datetime import date
from uuid import UUID

import httpx
import msgspec
import polars as pl
import polars.selectors as cs
from litestar import Controller, get
from msgspec import Struct

from app.core.config import settings
from app.core.models import BudgetDetailResponse


class Transaction(Struct, forbid_unknown_fields=True):
    id: UUID
    date: date
    amount: int

    account_id: UUID
    account: str

    payee_id: UUID
    payee: str

    category_id: UUID
    category: str

    category_group_id: UUID
    category_group: str


def construct_df(models: Sequence[Struct] | None):
    return pl.LazyFrame(
        [msgspec.to_builtins(model) for model in models] if models else None,
        infer_schema_length=None,
    )


class TransactionController(Controller):
    path = "/transactions"

    @get()
    async def list_transactions(self, client: httpx.AsyncClient) -> list[Transaction]:
        response = (
            await client.get(
                "/budgets/last-used",
                headers={"Authorization": f"Bearer {settings.YNAB_TOKEN}"},
            )
        ).raise_for_status()

        budget = msgspec.json.decode(
            response.content, type=BudgetDetailResponse
        ).data.budget

        subtransactions = construct_df(budget.subtransactions).select(
            "amount", "payee_id", "category_id", id="transaction_id"
        )
        transactions = (
            construct_df(budget.transactions)
            .select("id", "date", "amount", "account_id", "payee_id", "category_id")
            .update(subtransactions, how="left", on="id")
        )

        accounts = construct_df(budget.accounts).select(account_id="id", account="name")

        payees = construct_df(budget.payees).select(payee_id="id", payee="name")

        category_groups = construct_df(budget.category_groups).select(
            category_group_id="id", category_group="name"
        )
        categories = (
            construct_df(budget.categories)
            .select("category_group_id", category_id="id", category="name")
            .join(category_groups, on="category_group_id")
        )

        transactions = (
            transactions.join(accounts, how="left", on="account_id")
            .join(payees, how="left", on="payee_id")
            .join(categories, how="left", on="category_id")
            # Handle invalid UUIDs
            .with_columns(cs.ends_with("id").str.split("_").list.first())
            .filter(
                # Exclude transfer transactions
                pl.col("category").is_not_null(),
                # Exclude inflow transactions
                pl.concat_list("category_group", "category")
                != ["Internal Master Category", "Inflow: Ready to Assign"],
            )
            .collect()
            .to_dicts()
        )

        return msgspec.convert(transactions, list[Transaction])
