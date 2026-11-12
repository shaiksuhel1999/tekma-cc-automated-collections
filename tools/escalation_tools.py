
from langchain.tools import tool

from tools.mock_database import (
    ESCALATIONS,
    CUSTOMERS,
    generate_reference,
    normalize_customer_id
)


ESCALATION_QUEUES = [
    "COLLECTION_OFFICER",
    "COMPLIANCE_TEAM",
    "FRAUD_INVESTIGATION",
    "PAYMENT_OPERATIONS",
    "DISPUTE_INVESTIGATION",
    "FINANCIAL_HARDSHIP_TEAM",
    "MANAGEMENT_REVIEW"
]


@tool
def get_escalation_queue() -> dict:
    """
    Retrieve available human escalation departments.
    """

    return {
        "available_queues": ESCALATION_QUEUES
    }


@tool
def create_escalation_case(
    customer_id: str,
    department: str,
    reason: str,
    case_summary: str
) -> dict:
    """
    Create a human review case for a customer.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    if department not in ESCALATION_QUEUES:
        return {"error": "Invalid escalation department"}

    if not reason.strip() or not case_summary.strip():
        return {"error": "Reason and summary are required"}

    reference = generate_reference("ESC")

    ESCALATIONS[reference] = {
        "case_id": reference,
        "customer_id": customer_id,
        "department": department,
        "reason": reason,
        "summary": case_summary,
        "status": "PENDING_REVIEW",
        "notes": []
    }

    return {
        "case_id": reference,
        "department": department,
        "status": "PENDING_REVIEW"
    }


@tool
def get_escalation_status(case_id: str) -> dict:
    """
    Retrieve the status of an existing human escalation.
    """

    case = ESCALATIONS.get(case_id)

    if not case:
        return {"error": "Escalation case not found"}

    return {
        "case_id": case_id,
        "status": case["status"],
        "department": case["department"]
    }


@tool
def add_escalation_note(
    case_id: str,
    note: str
) -> dict:
    """
    Add a note to an existing escalation case.
    """

    case = ESCALATIONS.get(case_id)

    if not case:
        return {"error": "Escalation case not found"}

    if not note.strip():
        return {"error": "Note cannot be empty"}

    case["notes"].append(note)

    return {
        "case_id": case_id,
        "status": "NOTE_ADDED"
    }
