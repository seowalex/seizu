# generated by datamodel-codegen:
#   filename:  https://api.ynab.com/papi/open_api_spec.yaml

from __future__ import annotations

from enum import Enum
from typing import Annotated

from msgspec import Meta, Struct


class ErrorDetail(Struct, kw_only=True):
    id: str
    name: str
    detail: str


class User(Struct, kw_only=True):
    id: str


class DateFormat(Struct, kw_only=True):
    format: str


class CurrencyFormat(Struct, kw_only=True):
    iso_code: str
    example_format: str
    decimal_digits: int
    decimal_separator: str
    symbol_first: bool
    group_separator: str
    currency_symbol: str
    display_symbol: bool


class BudgetSettings(Struct, kw_only=True):
    date_format: DateFormat
    currency_format: CurrencyFormat


LoanAccountPeriodicValue = dict[str, int] | None


class AccountType(Enum):
    CHECKING = 'checking'
    SAVINGS = 'savings'
    CASH = 'cash'
    CREDIT_CARD = 'creditCard'
    LINE_OF_CREDIT = 'lineOfCredit'
    OTHER_ASSET = 'otherAsset'
    OTHER_LIABILITY = 'otherLiability'
    MORTGAGE = 'mortgage'
    AUTO_LOAN = 'autoLoan'
    STUDENT_LOAN = 'studentLoan'
    PERSONAL_LOAN = 'personalLoan'
    MEDICAL_DEBT = 'medicalDebt'
    OTHER_DEBT = 'otherDebt'


class CategoryGroup(Struct, kw_only=True):
    id: str
    name: str
    hidden: Annotated[
        bool, Meta(description='Whether or not the category group is hidden')
    ]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests.'
        ),
    ]


class GoalTypeEnum(Enum):
    TB = 'TB'
    TBD = 'TBD'
    MF = 'MF'
    NEED = 'NEED'
    DEBT = 'DEBT'


GoalType = (
    Annotated[
        GoalTypeEnum,
        Meta(
            description="The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')"
        ),
    ]
    | None
)


class Category(Struct, kw_only=True):
    id: str
    category_group_id: str
    name: str
    hidden: Annotated[bool, Meta(description='Whether or not the category is hidden')]
    budgeted: Annotated[int, Meta(description='Budgeted amount in milliunits format')]
    activity: Annotated[int, Meta(description='Activity amount in milliunits format')]
    balance: Annotated[int, Meta(description='Balance in milliunits format')]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.'
        ),
    ]
    category_group_name: str | None = None
    original_category_group_id: (
        Annotated[
            str,
            Meta(description='DEPRECATED: No longer used.  Value will always be null.'),
        ]
        | None
    ) = None
    note: str | None = None
    goal_type: (
        Annotated[
            GoalType,
            Meta(
                description="The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')"
            ),
        ]
        | None
    ) = None
    goal_needs_whole_amount: (
        Annotated[
            bool,
            Meta(
                description='Indicates the monthly rollover behavior for "NEED"-type goals. When "true", the goal will always ask for the target amount in the new month ("Set Aside"). When "false", previous month category funding is used ("Refill"). For other goal types, this field will be null.'
            ),
        ]
        | None
    ) = None
    goal_day: (
        Annotated[
            int,
            Meta(
                description="A day offset modifier for the goal's due date. When goal_cadence is 2 (Weekly), this value specifies which day of the week the goal is due (0 = Sunday, 6 = Saturday). Otherwise, this value specifies which day of the month the goal is due (1 = 1st, 31 = 31st, null = Last day of Month)."
            ),
        ]
        | None
    ) = None
    goal_cadence: (
        Annotated[
            int,
            Meta(
                description="The goal cadence. Value in range 0-14. There are two subsets of these values which behave differently. For values 0, 1, 2, and 13, the goal's due date repeats every goal_cadence * goal_cadence_frequency, where 0 = None, 1 = Monthly, 2 = Weekly, and 13 = Yearly. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month. For values 3-12 and 14, goal_cadence_frequency is ignored and the goal's due date repeats every goal_cadence, where 3 = Every 2 Months, 4 = Every 3 Months, ..., 12 = Every 11 Months, and 14 = Every 2 Years."
            ),
        ]
        | None
    ) = None
    goal_cadence_frequency: (
        Annotated[
            int,
            Meta(
                description="The goal cadence frequency. When goal_cadence is 0, 1, 2, or 13, a goal's due date repeats every goal_cadence * goal_cadence_frequency. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month.  When goal_cadence is 3-12 or 14, goal_cadence_frequency is ignored."
            ),
        ]
        | None
    ) = None
    goal_creation_month: (
        Annotated[str, Meta(description='The month a goal was created')] | None
    ) = None
    goal_target: (
        Annotated[int, Meta(description='The goal target amount in milliunits')] | None
    ) = None
    goal_target_month: (
        Annotated[
            str,
            Meta(
                description='The original target month for the goal to be completed.  Only some goal types specify this date.'
            ),
        ]
        | None
    ) = None
    goal_percentage_complete: (
        Annotated[int, Meta(description='The percentage completion of the goal')] | None
    ) = None
    goal_months_to_budget: (
        Annotated[
            int,
            Meta(
                description='The number of months, including the current month, left in the current goal period.'
            ),
        ]
        | None
    ) = None
    goal_under_funded: (
        Annotated[
            int,
            Meta(
                description="The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period. This amount will generally correspond to the 'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month."
            ),
        ]
        | None
    ) = None
    goal_overall_funded: (
        Annotated[
            int,
            Meta(
                description='The total amount funded towards the goal within the current goal period.'
            ),
        ]
        | None
    ) = None
    goal_overall_left: (
        Annotated[
            int,
            Meta(
                description='The amount of funding still needed to complete the goal within the current goal period.'
            ),
        ]
        | None
    ) = None


class Data8(Struct, kw_only=True):
    category: Category
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class SaveCategoryResponse(Struct, kw_only=True):
    data: Data8


class Payee(Struct, kw_only=True):
    id: str
    name: str
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the payee has been deleted.  Deleted payees will only be included in delta requests.'
        ),
    ]
    transfer_account_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer payee, the `account_id` to which this payee transfers to'
            ),
        ]
        | None
    ) = None


class PayeeLocation(Struct, kw_only=True):
    id: str
    payee_id: str
    latitude: str
    longitude: str
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the payee location has been deleted.  Deleted payee locations will only be included in delta requests.'
        ),
    ]


class SaveSubTransaction(Struct, kw_only=True):
    amount: Annotated[
        int, Meta(description='The subtransaction amount in milliunits format.')
    ]
    payee_id: (
        Annotated[str, Meta(description='The payee for the subtransaction.')] | None
    ) = None
    payee_name: (
        Annotated[
            str,
            Meta(
                description='The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee.',
                max_length=200,
            ),
        ]
        | None
    ) = None
    category_id: (
        Annotated[
            str,
            Meta(
                description='The category for the subtransaction.  Credit Card Payment categories are not permitted and will be ignored if supplied.'
            ),
        ]
        | None
    ) = None
    memo: Annotated[str, Meta(max_length=500)] | None = None


class DebtTransactionTypeEnum(Enum):
    PAYMENT = 'payment'
    REFUND = 'refund'
    FEE = 'fee'
    INTEREST = 'interest'
    ESCROW = 'escrow'
    BALANCE_ADJUSTMENT = 'balanceAdjustment'
    CREDIT = 'credit'
    CHARGE = 'charge'


DebtTransactionType = (
    Annotated[
        DebtTransactionTypeEnum,
        Meta(
            description='If the transaction is a debt/loan account transaction, the type of transaction'
        ),
    ]
    | None
)


class Type(Enum):
    TRANSACTION = 'transaction'
    SUBTRANSACTION = 'subtransaction'


class SavePayee(Struct, kw_only=True):
    name: (
        Annotated[
            str,
            Meta(
                description='The name of the payee. The name must be a maximum of 500 characters.',
                max_length=500,
            ),
        ]
        | None
    ) = None


class SaveCategory(Struct, kw_only=True):
    name: str | None = None
    note: str | None = None
    category_group_id: str | None = None


class SaveMonthCategory(Struct, kw_only=True):
    budgeted: Annotated[int, Meta(description='Budgeted amount in milliunits format')]


class Data18(Struct, kw_only=True):
    transaction_ids: Annotated[
        list[str], Meta(description='The list of transaction ids that were imported.')
    ]


class TransactionsImportResponse(Struct, kw_only=True):
    data: Data18


class Bulk(Struct, kw_only=True):
    transaction_ids: Annotated[
        list[str], Meta(description='The list of Transaction ids that were created.')
    ]
    duplicate_import_ids: Annotated[
        list[str],
        Meta(
            description='If any Transactions were not created because they had an `import_id` matching a transaction already on the same account, the specified import_id(s) will be included in this list.'
        ),
    ]


class Data19(Struct, kw_only=True):
    bulk: Bulk


class BulkResponse(Struct, kw_only=True):
    data: Data19


class SubTransaction(Struct, kw_only=True):
    id: str
    transaction_id: str
    amount: Annotated[
        int, Meta(description='The subtransaction amount in milliunits format')
    ]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.'
        ),
    ]
    memo: str | None = None
    payee_id: str | None = None
    payee_name: str | None = None
    category_id: str | None = None
    category_name: str | None = None
    transfer_account_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer, the account_id which the subtransaction transfers to'
            ),
        ]
        | None
    ) = None
    transfer_transaction_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer, the id of transaction on the other side of the transfer'
            ),
        ]
        | None
    ) = None


class Frequency(Enum):
    NEVER = 'never'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    EVERY_OTHER_WEEK = 'everyOtherWeek'
    TWICE_A_MONTH = 'twiceAMonth'
    EVERY4_WEEKS = 'every4Weeks'
    MONTHLY = 'monthly'
    EVERY_OTHER_MONTH = 'everyOtherMonth'
    EVERY3_MONTHS = 'every3Months'
    EVERY4_MONTHS = 'every4Months'
    TWICE_A_YEAR = 'twiceAYear'
    YEARLY = 'yearly'
    EVERY_OTHER_YEAR = 'everyOtherYear'


class ScheduledSubTransaction(Struct, kw_only=True):
    id: str
    scheduled_transaction_id: str
    amount: Annotated[
        int,
        Meta(description='The scheduled subtransaction amount in milliunits format'),
    ]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the scheduled subtransaction has been deleted. Deleted scheduled subtransactions will only be included in delta requests.'
        ),
    ]
    memo: str | None = None
    payee_id: str | None = None
    category_id: str | None = None
    transfer_account_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer, the account_id which the scheduled subtransaction transfers to'
            ),
        ]
        | None
    ) = None


class MonthSummary(Struct, kw_only=True):
    month: str
    income: Annotated[
        int,
        Meta(
            description="The total amount of transactions categorized to 'Inflow: Ready to Assign' in the month"
        ),
    ]
    budgeted: Annotated[int, Meta(description='The total amount budgeted in the month')]
    activity: Annotated[
        int,
        Meta(
            description="The total amount of transactions in the month, excluding those categorized to 'Inflow: Ready to Assign'"
        ),
    ]
    to_be_budgeted: Annotated[
        int, Meta(description="The available amount for 'Ready to Assign'")
    ]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the month has been deleted.  Deleted months will only be included in delta requests.'
        ),
    ]
    note: str | None = None
    age_of_money: (
        Annotated[int, Meta(description='The Age of Money as of the month')] | None
    ) = None


class MonthDetail(MonthSummary, kw_only=True):
    categories: Annotated[
        list[Category],
        Meta(
            description='The budget month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified.'
        ),
    ]


class TransactionFlagColorEnum(Enum):
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    PURPLE = 'purple'


TransactionFlagColor = (
    Annotated[TransactionFlagColorEnum, Meta(description='The transaction flag')] | None
)


TransactionFlagName = (
    Annotated[str, Meta(description='The customized name of a transaction flag')] | None
)


class TransactionClearedStatus(Enum):
    CLEARED = 'cleared'
    UNCLEARED = 'uncleared'
    RECONCILED = 'reconciled'


class ErrorResponse(Struct, kw_only=True):
    error: ErrorDetail


class Data(Struct, kw_only=True):
    user: User


class UserResponse(Struct, kw_only=True):
    data: Data


class Data3(Struct, kw_only=True):
    settings: BudgetSettings


class BudgetSettingsResponse(Struct, kw_only=True):
    data: Data3


class Account(Struct, kw_only=True):
    id: str
    name: str
    type: AccountType
    on_budget: Annotated[
        bool, Meta(description='Whether this account is on budget or not')
    ]
    closed: Annotated[bool, Meta(description='Whether this account is closed or not')]
    balance: Annotated[
        int, Meta(description='The current balance of the account in milliunits format')
    ]
    cleared_balance: Annotated[
        int,
        Meta(
            description='The current cleared balance of the account in milliunits format'
        ),
    ]
    uncleared_balance: Annotated[
        int,
        Meta(
            description='The current uncleared balance of the account in milliunits format'
        ),
    ]
    transfer_payee_id: Annotated[
        str,
        Meta(
            description='The payee id which should be used when transferring to this account'
        ),
    ]
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.'
        ),
    ]
    note: str | None = None
    direct_import_linked: (
        Annotated[
            bool,
            Meta(
                description='Whether or not the account is linked to a financial institution for automatic transaction import.'
            ),
        ]
        | None
    ) = None
    direct_import_in_error: (
        Annotated[
            bool,
            Meta(
                description='If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.'
            ),
        ]
        | None
    ) = None
    last_reconciled_at: (
        Annotated[
            str,
            Meta(
                description='A date/time specifying when the account was last reconciled.'
            ),
        ]
        | None
    ) = None
    debt_original_balance: (
        Annotated[
            int,
            Meta(
                description='The original debt/loan account balance, specified in milliunits format.'
            ),
        ]
        | None
    ) = None
    debt_interest_rates: LoanAccountPeriodicValue | None = None
    debt_minimum_payments: LoanAccountPeriodicValue | None = None
    debt_escrow_amounts: LoanAccountPeriodicValue | None = None


class SaveAccount(Struct, kw_only=True):
    name: Annotated[str, Meta(description='The name of the account')]
    type: AccountType
    balance: Annotated[
        int, Meta(description='The current balance of the account in milliunits format')
    ]


class Data7(Struct, kw_only=True):
    category: Category


class CategoryResponse(Struct, kw_only=True):
    data: Data7


class CategoryGroupWithCategories(CategoryGroup, kw_only=True):
    categories: Annotated[
        list[Category],
        Meta(
            description='Category group categories.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).'
        ),
    ]


class Data9(Struct, kw_only=True):
    payees: list[Payee]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class PayeesResponse(Struct, kw_only=True):
    data: Data9


class Data10(Struct, kw_only=True):
    payee: Payee


class PayeeResponse(Struct, kw_only=True):
    data: Data10


class Data11(Struct, kw_only=True):
    payee: Payee
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class SavePayeeResponse(Struct, kw_only=True):
    data: Data11


class Data12(Struct, kw_only=True):
    payee_locations: list[PayeeLocation]


class PayeeLocationsResponse(Struct, kw_only=True):
    data: Data12


class Data13(Struct, kw_only=True):
    payee_location: PayeeLocation


class PayeeLocationResponse(Struct, kw_only=True):
    data: Data13


class SaveTransactionWithOptionalFields(Struct, kw_only=True):
    account_id: str | None = None
    date: (
        Annotated[
            str,
            Meta(
                description='The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.'
            ),
        ]
        | None
    ) = None
    amount: (
        Annotated[
            int,
            Meta(
                description='The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.'
            ),
        ]
        | None
    ) = None
    payee_id: (
        Annotated[
            str,
            Meta(
                description='The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `transfer_payee_id` on the account resource.'
            ),
        ]
        | None
    ) = None
    payee_name: (
        Annotated[
            str,
            Meta(
                description='The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.',
                max_length=200,
            ),
        ]
        | None
    ) = None
    category_id: (
        Annotated[
            str,
            Meta(
                description='The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.'
            ),
        ]
        | None
    ) = None
    memo: Annotated[str, Meta(max_length=500)] | None = None
    cleared: TransactionClearedStatus | None = None
    approved: (
        Annotated[
            bool,
            Meta(
                description='Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.'
            ),
        ]
        | None
    ) = None
    flag_color: TransactionFlagColor | None = None
    subtransactions: (
        Annotated[
            list[SaveSubTransaction],
            Meta(
                description='An array of subtransactions to configure a transaction as a split. Updating `subtransactions` on an existing split transaction is not supported.'
            ),
        ]
        | None
    ) = None


class TransactionSummary(Struct, kw_only=True):
    id: str
    date: Annotated[
        str, Meta(description='The transaction date in ISO format (e.g. 2016-12-01)')
    ]
    amount: Annotated[
        int, Meta(description='The transaction amount in milliunits format')
    ]
    cleared: TransactionClearedStatus
    approved: Annotated[
        bool, Meta(description='Whether or not the transaction is approved')
    ]
    account_id: str
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.'
        ),
    ]
    memo: str | None = None
    flag_color: TransactionFlagColor | None = None
    flag_name: TransactionFlagName | None = None
    payee_id: str | None = None
    category_id: str | None = None
    transfer_account_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer transaction, the account to which it transfers'
            ),
        ]
        | None
    ) = None
    transfer_transaction_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer transaction, the id of transaction on the other side of the transfer'
            ),
        ]
        | None
    ) = None
    matched_transaction_id: (
        Annotated[
            str,
            Meta(
                description='If transaction is matched, the id of the matched transaction'
            ),
        ]
        | None
    ) = None
    import_id: (
        Annotated[
            str,
            Meta(
                description="If the transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'."
            ),
        ]
        | None
    ) = None
    import_payee_name: (
        Annotated[
            str,
            Meta(
                description='If the transaction was imported, the payee name that was used when importing and before applying any payee rename rules'
            ),
        ]
        | None
    ) = None
    import_payee_name_original: (
        Annotated[
            str,
            Meta(
                description='If the transaction was imported, the original payee name as it appeared on the statement'
            ),
        ]
        | None
    ) = None
    debt_transaction_type: (
        Annotated[
            DebtTransactionType,
            Meta(
                description='If the transaction is a debt/loan account transaction, the type of transaction'
            ),
        ]
        | None
    ) = None


class TransactionDetail(TransactionSummary, kw_only=True):
    account_name: str
    subtransactions: Annotated[
        list[SubTransaction],
        Meta(description='If a split transaction, the subtransactions.'),
    ]
    payee_name: str | None = None
    category_name: (
        Annotated[
            str,
            Meta(
                description="The name of the category.  If a split transaction, this will be 'Split'."
            ),
        ]
        | None
    ) = None


class HybridTransaction(TransactionSummary, kw_only=True):
    type: Annotated[
        Type,
        Meta(
            description='Whether the hybrid transaction represents a regular transaction or a subtransaction'
        ),
    ]
    account_name: str
    parent_transaction_id: (
        Annotated[
            str,
            Meta(
                description='For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.'
            ),
        ]
        | None
    ) = None
    payee_name: str | None = None
    category_name: (
        Annotated[
            str,
            Meta(
                description="The name of the category.  If a split transaction, this will be 'Split'."
            ),
        ]
        | None
    ) = None


class PatchPayeeWrapper(Struct, kw_only=True):
    payee: SavePayee


class PatchCategoryWrapper(Struct, kw_only=True):
    category: SaveCategory


class PatchMonthCategoryWrapper(Struct, kw_only=True):
    category: SaveMonthCategory


class BulkTransactions(Struct, kw_only=True):
    transactions: list[SaveTransactionWithOptionalFields]


class SaveScheduledTransaction(Struct, kw_only=True):
    account_id: str
    date: Annotated[
        str,
        Meta(
            description='The scheduled transaction date in ISO format (e.g. 2016-12-01).  This should be a future date no more than 5 years into the future.'
        ),
    ]
    amount: (
        Annotated[
            int,
            Meta(description='The scheduled transaction amount in milliunits format.'),
        ]
        | None
    ) = None
    payee_id: (
        Annotated[
            str,
            Meta(
                description='The payee for the scheduled transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `transfer_payee_id` on the account resource.'
            ),
        ]
        | None
    ) = None
    payee_name: (
        Annotated[
            str,
            Meta(
                description='The payee name for the the scheduled transaction.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a payee with the same name or (2) creation of a new payee.',
                max_length=200,
            ),
        ]
        | None
    ) = None
    category_id: (
        Annotated[
            str,
            Meta(
                description='The category for the scheduled transaction. Credit Card Payment categories are not permitted. Creating a split scheduled transaction is not currently supported.'
            ),
        ]
        | None
    ) = None
    memo: Annotated[str, Meta(max_length=500)] | None = None
    flag_color: TransactionFlagColor | None = None
    frequency: Frequency | None = None


class ScheduledTransactionSummary(Struct, kw_only=True):
    id: str
    date_first: Annotated[
        str,
        Meta(
            description='The first date for which the Scheduled Transaction was scheduled.'
        ),
    ]
    date_next: Annotated[
        str,
        Meta(
            description='The next date for which the Scheduled Transaction is scheduled.'
        ),
    ]
    frequency: Frequency
    amount: Annotated[
        int, Meta(description='The scheduled transaction amount in milliunits format')
    ]
    account_id: str
    deleted: Annotated[
        bool,
        Meta(
            description='Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.'
        ),
    ]
    memo: str | None = None
    flag_color: TransactionFlagColor | None = None
    flag_name: TransactionFlagName | None = None
    payee_id: str | None = None
    category_id: str | None = None
    transfer_account_id: (
        Annotated[
            str,
            Meta(
                description='If a transfer, the account_id which the scheduled transaction transfers to'
            ),
        ]
        | None
    ) = None


class ScheduledTransactionDetail(ScheduledTransactionSummary, kw_only=True):
    account_name: str
    subtransactions: Annotated[
        list[ScheduledSubTransaction],
        Meta(description='If a split scheduled transaction, the subtransactions.'),
    ]
    payee_name: str | None = None
    category_name: (
        Annotated[
            str,
            Meta(
                description="The name of the category.  If a split scheduled transaction, this will be 'Split'."
            ),
        ]
        | None
    ) = None


class Data22(Struct, kw_only=True):
    months: list[MonthSummary]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class MonthSummariesResponse(Struct, kw_only=True):
    data: Data22


class Data23(Struct, kw_only=True):
    month: MonthDetail


class MonthDetailResponse(Struct, kw_only=True):
    data: Data23


class BudgetSummary(Struct, kw_only=True):
    id: str
    name: str
    last_modified_on: (
        Annotated[
            str,
            Meta(
                description='The last time any changes were made to the budget from either a web or mobile client'
            ),
        ]
        | None
    ) = None
    first_month: (
        Annotated[str, Meta(description='The earliest budget month')] | None
    ) = None
    last_month: Annotated[str, Meta(description='The latest budget month')] | None = (
        None
    )
    date_format: DateFormat | None = None
    currency_format: CurrencyFormat | None = None
    accounts: (
        Annotated[
            list[Account],
            Meta(
                description='The budget accounts (only included if `include_accounts=true` specified as query parameter)'
            ),
        ]
        | None
    ) = None


class BudgetDetail(BudgetSummary, kw_only=True):
    accounts: list[Account] | None = None
    payees: list[Payee] | None = None
    payee_locations: list[PayeeLocation] | None = None
    category_groups: list[CategoryGroup] | None = None
    categories: list[Category] | None = None
    months: list[MonthDetail] | None = None
    transactions: list[TransactionSummary] | None = None
    subtransactions: list[SubTransaction] | None = None
    scheduled_transactions: list[ScheduledTransactionSummary] | None = None
    scheduled_subtransactions: list[ScheduledSubTransaction] | None = None


class Data4(Struct, kw_only=True):
    accounts: list[Account]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class AccountsResponse(Struct, kw_only=True):
    data: Data4


class Data5(Struct, kw_only=True):
    account: Account


class AccountResponse(Struct, kw_only=True):
    data: Data5


class PostAccountWrapper(Struct, kw_only=True):
    account: SaveAccount


class Data6(Struct, kw_only=True):
    category_groups: list[CategoryGroupWithCategories]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class CategoriesResponse(Struct, kw_only=True):
    data: Data6


class Data14(Struct, kw_only=True):
    transactions: list[TransactionDetail]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class TransactionsResponse(Struct, kw_only=True):
    data: Data14


class Data15(Struct, kw_only=True):
    transactions: list[HybridTransaction]
    server_knowledge: (
        Annotated[int, Meta(description='The knowledge of the server')] | None
    ) = None


class HybridTransactionsResponse(Struct, kw_only=True):
    data: Data15


class ExistingTransaction(SaveTransactionWithOptionalFields, kw_only=True):
    pass


class NewTransaction(SaveTransactionWithOptionalFields, kw_only=True):
    import_id: (
        Annotated[
            str,
            Meta(
                description='If specified, a new transaction will be assigned this `import_id` and considered "imported".  We will also attempt to match this imported transaction to an existing "user-entered" transaction on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: \'YNAB:[milliunit_amount]:[iso_date]:[occurrence]\'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of \'YNAB:-294230:2015-12-30:1\'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be \'YNAB:-294230:2015-12-30:2\'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a "user-entered" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).',
                max_length=36,
            ),
        ]
        | None
    ) = None


class SaveTransactionWithIdOrImportId(SaveTransactionWithOptionalFields, kw_only=True):
    id: (
        Annotated[
            str,
            Meta(
                description='If specified, this id will be used to lookup a transaction by its `id` for the purpose of updating the transaction itself. If not specified, an `import_id` should be supplied.'
            ),
        ]
        | None
    ) = None
    import_id: (
        Annotated[
            str,
            Meta(
                description='If specified, this id will be used to lookup a transaction by its `import_id` for the purpose of updating the transaction itself. If not specified, an `id` should be supplied.  You may not provide both an `id` and an `import_id` and updating an `import_id` on an existing transaction is not allowed.',
                max_length=36,
            ),
        ]
        | None
    ) = None


class Data16(Struct, kw_only=True):
    transaction_ids: Annotated[
        list[str], Meta(description='The transaction ids that were saved')
    ]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]
    transaction: TransactionDetail | None = None
    transactions: (
        Annotated[
            list[TransactionDetail],
            Meta(
                description='If multiple transactions were specified, the transactions that were saved'
            ),
        ]
        | None
    ) = None
    duplicate_import_ids: (
        Annotated[
            list[str],
            Meta(
                description='If multiple transactions were specified, a list of import_ids that were not created because of an existing `import_id` found on the same account'
            ),
        ]
        | None
    ) = None


class SaveTransactionsResponse(Struct, kw_only=True):
    data: Data16


class Data17(Struct, kw_only=True):
    transaction: TransactionDetail


class TransactionResponse(Struct, kw_only=True):
    data: Data17


class Data20(Struct, kw_only=True):
    scheduled_transactions: list[ScheduledTransactionDetail]
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class ScheduledTransactionsResponse(Struct, kw_only=True):
    data: Data20


class Data21(Struct, kw_only=True):
    scheduled_transaction: ScheduledTransactionDetail


class ScheduledTransactionResponse(Struct, kw_only=True):
    data: Data21


class PostScheduledTransactionWrapper(Struct, kw_only=True):
    scheduled_transaction: SaveScheduledTransaction


class Data1(Struct, kw_only=True):
    budgets: list[BudgetSummary]
    default_budget: BudgetSummary | None = None


class BudgetSummaryResponse(Struct, kw_only=True):
    data: Data1


class Data2(Struct, kw_only=True):
    budget: BudgetDetail
    server_knowledge: Annotated[int, Meta(description='The knowledge of the server')]


class BudgetDetailResponse(Struct, kw_only=True):
    data: Data2


class PutTransactionWrapper(Struct, kw_only=True):
    transaction: ExistingTransaction


class PostTransactionsWrapper(Struct, kw_only=True):
    transaction: NewTransaction | None = None
    transactions: list[NewTransaction] | None = None


class PatchTransactionsWrapper(Struct, kw_only=True):
    transactions: list[SaveTransactionWithIdOrImportId]
