from prompts.payment_processing_prompt import PAYMENT_PROCESSING_PROMPT
from models.agent_response import AgentResponse
from tools.agent_tools import PAYMENT_PROCESSING_TOOLS

description = """
Specialist agent responsible for handling authorized
credit card payment operations.

Handles:
- Customer payment requests.
- Payment amount verification.
- Available payment methods.
- Payment initiation through authorized payment APIs.
- Payment transaction status.
- Payment confirmation and reconciliation.

Validates payment details and ensures explicit customer
authorization before initiating transactions.

Coordinates with the Dispute Resolution Agent when
payments are not reflected in customer accounts.

Never claims a payment was successful without confirmation
from the payment processing system.
"""


payment_processing_agent = {
    "name": "payment_processing_agent",
    "description": description,
    "tools": PAYMENT_PROCESSING_TOOLS,
    "system_prompt": PAYMENT_PROCESSING_PROMPT,
    "response_format": AgentResponse
}


