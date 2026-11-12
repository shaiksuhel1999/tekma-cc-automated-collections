from tools.agent_tools import PAYMENT_NEGOTIATION_TOOLS
from prompts.payment_negotiation_prompt import PAYMENT_NEGOTIATION_PROMPT
from models.agent_response import AgentResponse

description = """
Specialist agent responsible for handling credit card
repayment negotiations.

Handles customers who want to:
- Convert outstanding balances into installments.
- Request partial payment arrangements.
- Discuss repayment schedules.
- Explore available repayment options.
- Understand minimum payment requirements.

Retrieves account information, checks repayment eligibility,
evaluates available plans and presents permitted options.

Delegates financial hardship cases to the Financial
Assistance Agent.

Cannot independently approve settlements, waive fees
or modify repayment terms.
"""

payment_negotiation_agent = {
    "name": "payment_negotiation_agent",
    "description": description,
    "tools": PAYMENT_NEGOTIATION_TOOLS,
    "system_prompt": PAYMENT_NEGOTIATION_PROMPT,
    "response_format": AgentResponse
}



