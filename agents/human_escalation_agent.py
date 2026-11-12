from prompts.human_escalation_prompt import HUMAN_ESCALATION_PROMPT
from tools.agent_tools import HUMAN_ESCALATION_TOOLS
from models.agent_response import AgentResponse

description = """
Specialist agent responsible for coordinating cases that
require intervention from human collection officers,
compliance teams or banking operations teams.

Handles:
- Customer requests for human assistance.
- Complex repayment negotiations.
- Exceptional settlement requests.
- Suspected fraud and identity theft.
- Repeated unsuccessful collection interactions.
- Vulnerable customer situations.
- Compliance-related escalations.
- Unresolved disputes.

Collects relevant case information, prepares an escalation
summary, identifies the appropriate department and creates
a human review request through authorized tools.

Tracks escalation status when available.

Cannot independently resolve cases requiring human approval.
"""

human_escalation_agent = {
    "name": "human_escalation_agent",
    "description": description,
    "system_prompt": HUMAN_ESCALATION_PROMPT,
    "tools": HUMAN_ESCALATION_TOOLS,
    "response_format": AgentResponse
}

