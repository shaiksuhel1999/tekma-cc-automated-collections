from tools.agent_tools import DISPUTE_RESOLUTION_TOOLS
from prompts.dispute_resolution_prompt import DISPUTE_RESOLUTION_PROMPT
from models.agent_response import AgentResponse

description = """
Specialist agent responsible for handling credit card
billing disputes and transaction-related complaints.

Handles:
- Unauthorized transactions.
- Duplicate transactions.
- Incorrect transaction amounts.
- Unrecognized merchants.
- Incorrect fees or charges.
- Payment credited but not reflected in the account.

Collects relevant transaction information, verifies available
transaction records and initiates authorized dispute
investigation workflows.

Coordinates with the Payment Processing Agent when
payment reconciliation is required.

Escalates suspected fraud and unresolved disputes
to the appropriate investigation team.
"""

dispute_resolution_agent = {
    "name": "dispute_resolution_agent",
    "description": description,
    "system_prompt": DISPUTE_RESOLUTION_PROMPT,
    "tools": DISPUTE_RESOLUTION_TOOLS,
    "response_format": AgentResponse
}




