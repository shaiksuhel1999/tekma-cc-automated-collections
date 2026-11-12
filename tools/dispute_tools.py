
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    TRANSACTIONS,
    DISPUTES,
    generate_reference,
    normalize_customer_id
)


@tool
def get_transaction_history(customer_id: str) -> dict:
    """
    Retrieve posted credit card transactions
    for a customer.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    return {
        "customer_id": customer_id,
        "transactions": TRANSACTIONS.get(customer_id, [])
    }


@tool
def get_transaction_details(
    customer_id: str,
    transaction_id: str
) -> dict:
    """
    Retrieve details of a specific customer transaction.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    transaction = next(
        (
            t for t in TRANSACTIONS.get(customer_id, [])
            if t["transaction_id"] == transaction_id
        ),
        None
    )

    if not transaction:
        return {"error": "Transaction not found"}

    return transaction


@tool
def create_dispute_case(
    customer_id: str,
    transaction_id: str,
    dispute_category: str,
    customer_statement: str
) -> dict:
    """
    Create a dispute investigation case.

    Does not reverse transactions or guarantee refunds.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    transaction = next(
        (
            t for t in TRANSACTIONS.get(customer_id, [])
            if t["transaction_id"] == transaction_id
        ),
        None
    )

    if not transaction:
        return {"error": "Transaction not found"}

    allowed_categories = [
        "UNAUTHORIZED_TRANSACTION",
        "DUPLICATE_TRANSACTION",
        "INCORRECT_AMOUNT",
        "UNKNOWN_MERCHANT",
        "PAYMENT_NOT_REFLECTED",
        "INCORRECT_FEE",
        "OTHER"
    ]

    if dispute_category not in allowed_categories:
        return {"error": "Invalid dispute category"}

    if not customer_statement.strip():
        return {"error": "Customer statement is required"}

    reference = generate_reference("DISPUTE")

    DISPUTES[reference] = {
        "case_id": reference,
        "customer_id": customer_id,
        "transaction_id": transaction_id,
        "category": dispute_category,
        "customer_statement": customer_statement,
        "status": "OPEN"
    }

    return {
        "case_id": reference,
        "status": "OPEN",
        "message": "Dispute submitted for investigation"
    }


@tool
def get_dispute_status(case_id: str) -> dict:
    """
    Retrieve the current status of a dispute case.
    """

    dispute = DISPUTES.get(case_id)

    if not dispute:
        return {"error": "Dispute case not found"}

    return dispute
