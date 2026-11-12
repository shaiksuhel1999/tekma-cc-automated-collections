import os

from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent

from prompts.supervisor_prompt import SUPERVISOR_SYSTEM_PROMPT
from tools.agent_tools import SUPERVISOR_TOOLS

from agents.payment_reminder_agent import payment_reminder_agent
from agents.payment_negotiation_agent import payment_negotiation_agent
from agents.financial_assistance_agent import financial_assistance_agent
from agents.dispute_resolution_agent import dispute_resolution_agent
from agents.payment_processing_agent import payment_processing_agent
from agents.compliance_agent import compliance_agent
from agents.human_escalation_agent import human_escalation_agent

SPECIALIST_AGENTS = [
    payment_reminder_agent,
    payment_negotiation_agent,
    financial_assistance_agent,
    dispute_resolution_agent,
    payment_processing_agent,
    compliance_agent,
    human_escalation_agent
]


def create_supervisor():

    model = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0
    )

    supervisor = create_deep_agent(
        model=model,
        tools=SUPERVISOR_TOOLS,
        system_prompt=SUPERVISOR_SYSTEM_PROMPT,
        subagents=SPECIALIST_AGENTS
    )

    return supervisor
