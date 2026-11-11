from typing import Literal, Optional

from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    agent_name: str

    status: Literal[
        "SUCCESS",
        "NEEDS_INFORMATION",
        "ESCALATION_REQUIRED",
        "FAILED"
    ]

    intent: str
    summary: str = Field(
        description="Internal summary of the specialist's findings"
    )

    customer_message: str = Field(
        description="Professional response intended for the customer"
    )

    actions_taken: list[str] = Field(default_factory=list)

    pending_actions: list[str] = Field(default_factory=list)

    requires_human_review: bool = False

    escalation_reason: Optional[str] = None