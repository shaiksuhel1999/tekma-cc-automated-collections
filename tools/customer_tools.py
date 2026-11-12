
from langchain.tools import tool

from tools.mock_database import find_customers


@tool
def find_customer(identifier: str) -> dict:
    """
    Identify a customer and return their customer_id.

    Accepts a customer ID (e.g. CUST-1001 or 1001), a full or
    partial name, an email address, a phone number or the last
    four digits of the card.

    Returns only identifying details. Use the returned
    customer_id with the specialist agents for account data.
    If more than one customer matches, ask the customer for
    another identifier instead of guessing.
    """

    matches = find_customers(identifier)

    if not matches:
        return {
            "match_count": 0,
            "error": "No customer matches the supplied identifier"
        }

    return {
        "match_count": len(matches),
        "matches": [
            {
                "customer_id": customer["customer_id"],
                "name": customer["name"],
                "card_number_masked": customer["card_number_masked"]
            }
            for customer in matches
        ]
    }
