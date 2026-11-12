
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    HARDSHIP_PROGRAMS,
    HARDSHIP_REQUESTS,
    generate_reference,
    normalize_customer_id
)


HARDSHIP_CATEGORIES = [
    "JOB_LOSS",
    "INCOME_REDUCTION",
    "MEDICAL_EMERGENCY",
    "FAMILY_EMERGENCY"
]


@tool
def get_hardship_programs() -> dict:
    """
    Retrieve currently configured financial hardship
    assistance programs.
    """

    return {
        "programs": HARDSHIP_PROGRAMS
    }


@tool
def check_hardship_eligibility(
    customer_id: str,
    hardship_category: str
) -> dict:
    """
    Check basic mock eligibility for a hardship
    assistance program.

    Categories include JOB_LOSS, INCOME_REDUCTION,
    MEDICAL_EMERGENCY and FAMILY_EMERGENCY.
    """

    customer_id = normalize_customer_id(customer_id)
    account = CUSTOMERS.get(customer_id)

    if not account:
        return {"error": "Customer account not found"}

    hardship_category = hardship_category.strip().upper()

    if hardship_category not in HARDSHIP_CATEGORIES:
        return {"error": "Unsupported hardship category"}

    eligible = account["days_overdue"] >= 30

    return {
        "customer_id": customer_id,
        "hardship_category": hardship_category,
        "basic_eligibility": eligible,
        "requires_documentation": True,
        "requires_human_review": True,
        "final_approval": False
    }


@tool
def submit_hardship_request(
    customer_id: str,
    hardship_category: str,
    customer_statement: str
) -> dict:
    """
    Create a hardship assistance application
    for human review.

    This tool submits a request but does not approve it.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    hardship_category = hardship_category.strip().upper()

    if hardship_category not in HARDSHIP_CATEGORIES:
        return {"error": "Unsupported hardship category"}

    if not customer_statement.strip():
        return {"error": "Customer statement is required"}

    reference = generate_reference("HARDSHIP")

    HARDSHIP_REQUESTS[reference] = {
        "request_id": reference,
        "customer_id": customer_id,
        "hardship_category": hardship_category,
        "customer_statement": customer_statement,
        "status": "SUBMITTED_FOR_REVIEW"
    }

    return {
        "request_id": reference,
        "customer_id": customer_id,
        "hardship_category": hardship_category,
        "status": "SUBMITTED_FOR_REVIEW",
        "requires_human_review": True
    }
