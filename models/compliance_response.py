from pydantic import BaseModel, Field
from typing import Literal


class ComplianceResponse(BaseModel):

    validation_status: Literal[
        "APPROVED",
        "REJECTED",
        "NEEDS_REVIEW"
    ]

    compliance_score: int = Field(ge=0, le=100)

    identified_violations: list[str] = Field(
        default_factory=list
    )

    potential_risks: list[str] = Field(
        default_factory=list
    )

    policy_references: list[str] = Field(
        default_factory=list
    )

    required_corrections: list[str] = Field(
        default_factory=list
    )

    requires_human_review: bool = False

    summary: str