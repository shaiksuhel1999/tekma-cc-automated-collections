
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    COMPLIANCE_AUDITS,
    generate_reference,
    get_contact_restrictions_for,
    normalize_customer_id
)


COLLECTION_POLICIES = {
    "policy_version": "COLLECTION-POLICY-1.0",
    "rules": [
        "No threatening or intimidating communication",
        "No misleading statements",
        "Respect customer privacy",
        "Follow approved contact frequency limits",
        "Escalate vulnerable customer situations"
    ]
}


@tool
def get_collection_policy() -> dict:
    """
    Retrieve the currently configured collection
    communication and operational policies.
    """

    return COLLECTION_POLICIES


@tool
def get_contact_restrictions(customer_id: str) -> dict:
    """
    Retrieve contact restrictions for a customer.

    The returned values are illustrative development data.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    return get_contact_restrictions_for(customer_id)


@tool
def get_repayment_policy() -> dict:
    """
    Retrieve approved repayment and installment
    policy parameters.
    """

    return {
        "policy_version": "REPAYMENT-POLICY-1.0",
        "settlement_requires_approval": True,
        "fee_waiver_requires_approval": True,
        "installment_plans": [
            "EMI-3",
            "EMI-6",
            "EMI-12"
        ]
    }


@tool
def get_disclosure_requirements() -> dict:
    """
    Retrieve mandatory customer disclosures
    for collection communications.
    """

    return {
        "requirements": [
            "Clearly communicate outstanding amounts",
            "Explain applicable repayment terms",
            "Disclose applicable charges and interest",
            "Avoid misleading payment commitments"
        ]
    }


@tool
def record_compliance_audit(
    agent_name: str,
    validation_status: str,
    summary: str
) -> dict:
    """
    Record a compliance validation result for auditing.

    This records an assessment but does not itself
    authorize or block a financial transaction.
    """

    allowed_statuses = [
        "APPROVED",
        "REJECTED",
        "NEEDS_REVIEW"
    ]

    if validation_status not in allowed_statuses:
        return {"error": "Invalid validation status"}

    reference = generate_reference("AUDIT")

    COMPLIANCE_AUDITS[reference] = {
        "audit_id": reference,
        "agent_name": agent_name,
        "validation_status": validation_status,
        "summary": summary
    }

    return {
        "audit_id": reference,
        "status": "RECORDED"
    }
