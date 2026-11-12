from tools.agent_tools import COMPLIANCE_TOOLS
from prompts.compliance_prompt import COMPLIANCE_PROMPT
from models.compliance_response import ComplianceResponse

description = """
Specialist agent responsible for validating collection
activities, repayment proposals and customer communications
against applicable compliance requirements and bank policies.

Reviews:
- Collection communication content.
- Repayment and settlement proposals.
- Customer privacy and data handling.
- Collection frequency and contact restrictions.
- Required customer disclosures.
- Escalation and approval requirements.
- Potential harassment, coercion or misleading statements.

Identifies compliance violations, policy deviations and
potential regulatory risks.

Can block an operation from proceeding when validation
fails and require human compliance review.

Does not independently approve financial transactions,
settlements or exceptions.
"""

compliance_agent = {
    "name": "compliance_agent",
    "description": description,
    "system_prompt": COMPLIANCE_PROMPT,
    "tools": COMPLIANCE_TOOLS,
    "response_format": ComplianceResponse
}