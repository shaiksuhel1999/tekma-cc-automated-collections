from models.agent_response import AgentResponse
from tools.agent_tools import FINANCIAL_ASSISTANCE_TOOLS
from prompts.financial_assistant_prompt import FINANCIAL_ASSISTANCE_PROMPT

description = """
Specialist agent responsible for assisting credit card
customers experiencing financial hardship.

Handles customers facing:
- Job loss or unemployment.
- Reduced income.
- Medical or family emergencies.
- Temporary financial difficulties.
- Inability to meet minimum payment obligations.

Understands the customer's situation, checks available
hardship assistance programs and identifies suitable
support options.

Coordinates with the Payment Negotiation Agent when
repayment alternatives need to be evaluated.

Escalates exceptional hardship cases for human review.
"""


financial_assistance_agent = {
    "name": "financial_assistance_agent",
    "description": description,
    "tools": FINANCIAL_ASSISTANCE_TOOLS,
    "system_prompt": FINANCIAL_ASSISTANCE_PROMPT,
    "response_format": AgentResponse
}



