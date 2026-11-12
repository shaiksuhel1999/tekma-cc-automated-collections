from models.agent_response import AgentResponse
from tools.agent_tools import PAYMENT_REMINDER_TOOLS
from prompts.payment_remainder_prompt import PAYMENT_REMINDER_PROMPT

description = """
    Specialized Credit Card Payment Reminder Agent responsible
    for handling customer queries and communications related
    to credit card payment dues and overdue accounts.

    Its responsibilities include:

    1. Retrieve and communicate verified credit card account
       information, including outstanding balance, minimum
       amount due, payment due date and days overdue.

    2. Provide payment reminders for upcoming, missed and
       overdue credit card payments.

    3. Retrieve previous payment history and explain the
       current payment status, including successful, pending
       or failed payments where verified information exists.

    4. Help customers understand their outstanding dues,
       minimum payment obligations and applicable payment
       deadlines.

    5. Capture and document customer-stated payment
       commitments, such as an intended payment date or
       amount, when supported by the available tools.

    6. Provide professional, polite and non-threatening
       payment reminder messages based on verified account
       information.

    7. Identify customers who may need repayment negotiation,
       financial hardship assistance, dispute resolution or
       human intervention and recommend delegation to the
       appropriate specialist agent.

    Delegate requests involving overdue balances, payment
    deadlines, minimum dues, payment history, payment status
    explanations and payment commitments to this agent.

    IMPORTANT RESTRICTIONS:
    - Do not initiate or process payments.
    - Do not approve settlements, waive fees or modify
      repayment terms.
    - Do not invent account balances, due dates or payment
      statuses.
    - Do not threaten, intimidate or pressure customers.
    - Do not disclose confidential customer information.
    - Escalate requests outside its responsibilities to
      the appropriate specialist agent.
    """

payment_reminder_agent = {
    "name": "payment_reminder_agent",

    "description": description,

    "system_prompt": PAYMENT_REMINDER_PROMPT,

    "tools": PAYMENT_REMINDER_TOOLS,

    "response_format": AgentResponse
}
