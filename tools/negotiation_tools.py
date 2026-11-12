
from langchain.tools import tool

from tools.mock_database import (
    CUSTOMERS,
    REPAYMENT_PLANS,
    normalize_customer_id
)


@tool
def get_repayment_options(customer_id: str) -> dict:
    """
    Retrieve available installment repayment plans
    for a customer's credit card account.
    """

    customer_id = normalize_customer_id(customer_id)

    if customer_id not in CUSTOMERS:
        return {"error": "Customer account not found"}

    return {
        "customer_id": customer_id,
        "available_plans": [
            plan for plan in REPAYMENT_PLANS
            if plan["available"]
        ]
    }


@tool
def check_repayment_eligibility(
    customer_id: str,
    plan_id: str
) -> dict:
    """
    Check whether a customer meets the mock eligibility
    criteria for a particular installment plan.
    """

    customer_id = normalize_customer_id(customer_id)
    account = CUSTOMERS.get(customer_id)

    if not account:
        return {"error": "Customer account not found"}

    plan = next(
        (p for p in REPAYMENT_PLANS
         if p["plan_id"] == plan_id),
        None
    )

    if not plan or not plan["available"]:
        return {"eligible": False, "reason": "Plan unavailable"}

    # Illustrative development policy only.
    eligible = (
        account["outstanding_balance"] >= 5000
        and account["days_overdue"] <= 90
    )

    return {
        "customer_id": customer_id,
        "plan_id": plan_id,
        "eligible": eligible,
        "reason": (
            "Meets mock eligibility criteria"
            if eligible else
            "Does not meet mock eligibility criteria"
        ),
        "requires_final_approval": True
    }


@tool
def calculate_installment(
    principal: float,
    annual_interest_rate: float,
    months: int
) -> dict:
    """
    Calculate an illustrative fixed monthly EMI
    using the reducing-balance method.

    Uses only the supplied approved rate.
    Does not approve an actual repayment arrangement.
    """

    if principal <= 0:
        return {"error": "Principal must be positive"}

    if annual_interest_rate < 0 or months <= 0:
        return {"error": "Invalid interest rate or duration"}

    monthly_rate = annual_interest_rate / 1200

    if monthly_rate == 0:
        emi = principal / months
    else:
        factor = (1 + monthly_rate) ** months
        emi = principal * monthly_rate * factor / (factor - 1)

    return {
        "principal": round(principal, 2),
        "annual_interest_rate": annual_interest_rate,
        "months": months,
        "estimated_monthly_installment": round(emi, 2),
        "currency": "INR",
        "is_approved": False
    }
