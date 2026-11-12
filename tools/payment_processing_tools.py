
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    PAYMENT_REQUESTS,
    generate_reference,
    normalize_customer_id
)


@tool
def get_payment_methods(customer_id: str) -> dict:
    """
    Retrieve payment methods supported by the
    mock credit card payment system.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    return {
        "payment_methods": [
            "UPI",
            "NET_BANKING",
            "BANK_TRANSFER"
        ]
    }


@tool
def validate_payment_request(
    customer_id: str,
    amount: float
) -> dict:
    """
    Validate a requested payment amount against
    the customer's outstanding balance.
    """

    customer_id = normalize_customer_id(customer_id)
    account = CUSTOMERS.get(customer_id)

    if not account:
        return {"valid": False, "reason": "Account not found"}

    if amount <= 0:
        return {"valid": False, "reason": "Invalid amount"}

    if amount > account["outstanding_balance"]:
        return {
            "valid": False,
            "reason": "Amount exceeds outstanding balance"
        }

    return {
        "valid": True,
        "customer_id": customer_id,
        "amount": amount,
        "currency": "INR",
        "requires_customer_authorization": True
    }


@tool
def initiate_payment(
    customer_id: str,
    amount: float,
    authorization_reference: str
) -> dict:
    """
    Initiate a mock payment only when an authorization
    reference has been validated by the trusted backend.

    This development implementation is NOT a real
    payment gateway.
    """

    # In production, this reference must be verified
    # against a trusted authorization service.
    if not authorization_reference.startswith("AUTH-"):
        return {
            "status": "REJECTED",
            "reason": "Invalid authorization reference"
        }

    customer_id = normalize_customer_id(customer_id)
    account = CUSTOMERS.get(customer_id)

    if not account:
        return {"status": "FAILED", "reason": "Account not found"}

    if amount <= 0 or amount > account["outstanding_balance"]:
        return {"status": "FAILED", "reason": "Invalid amount"}

    reference = generate_reference("PAY")

    PAYMENT_REQUESTS[reference] = {
        "reference": reference,
        "customer_id": customer_id,
        "amount": amount,
        "status": "PENDING"
    }

    return {
        "payment_reference": reference,
        "status": "PENDING",
        "message": "Mock payment request created"
    }


@tool
def get_payment_status(payment_reference: str) -> dict:
    """
    Retrieve the status of an initiated payment.
    """

    payment = PAYMENT_REQUESTS.get(payment_reference)

    if not payment:
        return {"error": "Payment reference not found"}

    return payment
