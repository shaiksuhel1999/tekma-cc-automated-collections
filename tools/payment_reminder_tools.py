
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    PAYMENT_HISTORY,
    normalize_customer_id
)


@tool
def get_customer_account(customer_id: str) -> dict:
    """
    Retrieve verified credit card account information
    including outstanding balance, minimum due amount,
    payment status and days overdue.
    """

    customer_id = normalize_customer_id(customer_id)
    account = CUSTOMERS.get(customer_id)

    if not account:
        return {"error": "Customer account not found"}

    return account


@tool
def get_payment_history(customer_id: str) -> dict:
    """
    Retrieve previous credit card payments made by
    the specified customer.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    return {
        "customer_id": customer_id,
        "payments": PAYMENT_HISTORY.get(customer_id, [])
    }
