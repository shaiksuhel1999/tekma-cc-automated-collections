# Tekma — Credit Card Automated Collections

A multi-agent assistant for credit card collections. A **supervisor agent** talks to the customer, identifies who they are, and delegates the work to one of **seven specialist agents** (reminders, negotiation, hardship, disputes, payments, compliance, human escalation). Every specialist works only through tools backed by an in-memory **mock database**, so the whole system runs locally with no bank systems attached.

Built with [DeepAgents](https://pypi.org/project/deepagents/) on LangChain/LangGraph and an OpenAI chat model.

> Everything in `tools/mock_database.py` is illustrative development data. Nothing here is a real payment gateway, policy engine or customer record.

---

## How a request flows

```
Customer (terminal chat — main.py)
        │  full conversation history on every turn
        ▼
Supervisor agent  (agents/supervisor_agent.py)
        │  1. find_customer  → resolves name / phone / card last-4 / ID to a customer_id
        │  2. delegates with the customer_id and the customer's request
        ├── payment_reminder_agent       balances, minimum due, overdue status, payment history
        ├── payment_negotiation_agent    EMI plans, eligibility, installment estimates
        ├── financial_assistance_agent   hardship programs, eligibility, hardship requests
        ├── dispute_resolution_agent     transactions, dispute cases
        ├── payment_processing_agent     payment methods, validation, mock payment initiation
        ├── compliance_agent             policy, contact restrictions, disclosures, audit log
        └── human_escalation_agent       human review cases and notes
                 │  @tool functions (tools/*.py)
                 ▼
        tools/mock_database.py  — customers, payments, transactions, plans, programs
```

Two rules make the lookup work:

1. **The supervisor identifies the customer first.** It owns the `find_customer` tool and will ask for an identifier if none was given.
2. **Specialists cannot see the conversation.** The supervisor passes the `customer_id` and the customer's request in every delegation; the specialist then calls its own tools with that ID.

---

## Project layout

```
tekma-cc-automated-collections/
├── main.py                          # Terminal chat loop; keeps the conversation history
├── agents/
│   ├── supervisor_agent.py          # Builds the supervisor and registers SPECIALIST_AGENTS
│   ├── payment_reminder_agent.py
│   ├── payment_negotiation_agent.py
│   ├── financial_assistance_agent.py
│   ├── dispute_resolution_agent.py
│   ├── payment_processing_agent.py
│   ├── compliance_agent.py
│   └── human_escalation_agent.py
├── prompts/                         # One system prompt per agent
├── models/
│   ├── agent_response.py            # Structured output for six specialists
│   └── compliance_response.py       # Structured output for the compliance agent
└── tools/
    ├── mock_database.py             # All mock data + ID normalisation and search helpers
    ├── customer_tools.py            # find_customer (supervisor)
    ├── agent_tools.py               # Tool lists per agent
    ├── payment_reminder_tools.py
    ├── negotiation_tools.py
    ├── hardship_tools.py
    ├── dispute_tools.py
    ├── payment_processing_tools.py
    ├── compliance_tools.py
    └── escalation_tools.py
```

Each specialist is a config dict (`name`, `description`, `system_prompt`, `tools`, `response_format`). **An agent only exists for the supervisor if it is listed in `SPECIALIST_AGENTS`** in `agents/supervisor_agent.py`.

---

## Agents and their tools

| Agent | Tools |
|---|---|
| Supervisor | `find_customer` + delegation to the specialists |
| `payment_reminder_agent` | `get_customer_account`, `get_payment_history` |
| `payment_negotiation_agent` | `get_customer_account`, `get_repayment_options`, `check_repayment_eligibility`, `calculate_installment` |
| `financial_assistance_agent` | `get_customer_account`, `get_hardship_programs`, `check_hardship_eligibility`, `submit_hardship_request` |
| `dispute_resolution_agent` | `get_transaction_history`, `get_transaction_details`, `create_dispute_case`, `get_dispute_status` |
| `payment_processing_agent` | `get_payment_methods`, `validate_payment_request`, `initiate_payment`, `get_payment_status` |
| `compliance_agent` | `get_collection_policy`, `get_contact_restrictions`, `get_repayment_policy`, `get_disclosure_requirements`, `record_compliance_audit` |
| `human_escalation_agent` | `get_escalation_queue`, `create_escalation_case`, `get_escalation_status`, `add_escalation_note` |

---

## Mock customers (reference)

Data is consistent as of **2026-11-09** (`AS_OF_DATE`). Currency is INR.

| Customer ID | Name | Card | Balance | Min due | Due date | Days overdue | Status |
|---|---|---|---:|---:|---|---:|---|
| CUST-1001 | John Smith | …1234 | 45,000 | 5,000 | 2026-10-05 | 35 | OVERDUE |
| CUST-1002 | Priya Sharma | …5678 | 18,500 | 925 | 2026-11-20 | 0 | CURRENT |
| CUST-1003 | Rahul Verma | …9012 | 27,800 | 2,780 | 2026-10-28 | 12 | OVERDUE |
| CUST-1004 | Anita Desai | …3456 | 132,000 | 13,200 | 2026-09-05 | 65 | OVERDUE |
| CUST-1005 | Vikram Nair | …7890 | 88,000 | 22,000 | 2026-07-12 | 120 | DELINQUENT |
| CUST-1006 | Meera Iyer | …2468 | 3,200 | 500 | 2026-09-30 | 40 | OVERDUE |

Phones follow `+91-98765-0100N` and emails `first.last@example.com` (e.g. CUST-1003 → `+91-98765-01003`, `rahul.verma@example.com`).

### What each customer is for

| Customer | EMI eligible | Hardship eligible | Built-in scenario |
|---|:---:|:---:|---|
| CUST-1001 John Smith | Yes | Yes | The standard overdue case |
| CUST-1002 Priya Sharma | Yes | No | Nothing overdue; unknown merchant `TXN-2002` to dispute |
| CUST-1003 Rahul Verma | Yes | No | Duplicate charge `TXN-3001` / `TXN-3002`; a failed payment |
| CUST-1004 Anita Desai | Yes | Yes | Job loss; flagged as a vulnerable customer |
| CUST-1005 Vikram Nair | No | Yes | Over 90 days; phone and SMS contact restricted (email only) |
| CUST-1006 Meera Iyer | No | Yes | Balance below the EMI minimum; contestable late fee `TXN-6002`; a pending payment |

### Mock rules behind those columns

- **EMI eligibility** — balance of at least 5,000 **and** no more than 90 days overdue. Plans: `EMI-3` and `EMI-6` at 15% a year, `EMI-12` at 16%.
- **Hardship eligibility** — at least 30 days overdue. Categories: `JOB_LOSS`, `INCOME_REDUCTION`, `MEDICAL_EMERGENCY`, `FAMILY_EMERGENCY`. A request is always submitted for human review, never approved by the agent.
- **Payments** — amount must be positive and not exceed the balance; `initiate_payment` needs an authorization reference starting with `AUTH-`. Methods: `UPI`, `NET_BANKING`, `BANK_TRANSFER`.
- **Dispute categories** — `UNAUTHORIZED_TRANSACTION`, `DUPLICATE_TRANSACTION`, `INCORRECT_AMOUNT`, `UNKNOWN_MERCHANT`, `PAYMENT_NOT_REFLECTED`, `INCORRECT_FEE`, `OTHER`.
- **Escalation departments** — `COLLECTION_OFFICER`, `COMPLIANCE_TEAM`, `FRAUD_INVESTIGATION`, `PAYMENT_OPERATIONS`, `DISPUTE_INVESTIGATION`, `FINANCIAL_HARDSHIP_TEAM`, `MANAGEMENT_REVIEW`.

### How customers are found

- `find_customer` accepts a customer ID, a full or partial name (three letters or more), an email, a phone number (ten digits or more) or the last four digits of the card. It returns only the ID, name and masked card — never balances.
- Every tool that takes a `customer_id` accepts loose forms: `CUST-1001`, `cust-1001`, `CUST1001` and `1001` are the same customer.
- Records created during a run (disputes, escalations, payment requests, hardship requests, compliance audits) live in memory and are lost when the program exits.

---

## Setup

Requires **Python 3.11+** and an OpenAI API key.

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install deepagents langchain langchain-openai pydantic python-dotenv
```

Create a `.env` file in the project root (next to `main.py`):

```dotenv
OPENAI_API_KEY=sk-...
# Optional. Defaults to gpt-4o-mini.
OPENAI_MODEL=gpt-4o-mini
```

Keep `.env` out of version control.

---

## Run

From the project root:

```bash
python main.py
```

Type `exit` to stop. The conversation is remembered for the whole session, so the customer only has to identify themselves once.

### Conversations to try

| Say this | What it exercises |
|---|---|
| `Hi, I'm John Smith. How much do I owe?` | Lookup by name → reminder agent |
| `My customer id is 1003. I was charged twice by SkyWings Airlines.` | Loose ID → duplicate-charge dispute |
| `Card ending 3456. I lost my job and can't pay the minimum.` | Lookup by card → hardship (eligible, vulnerable) |
| `This is cust-1005, can I convert my balance to a 6 month EMI?` | EMI refused (over 90 days) → escalation path |
| `I'm Meera Iyer, why was I charged an 800 late fee?` | Fee dispute on `TXN-6002` |
| `priya.sharma@example.com — I don't recognise a 9,800 charge.` | Lookup by email → unknown merchant dispute |
| `What's my balance?` (with no identifier) | Supervisor asks who you are |

---

## Limits

- **No identity verification.** Anyone who knows a name or card last-4 is treated as that customer. A real system needs authentication before account data is disclosed.
- **In-memory only.** Nothing is persisted between runs.
- **Mock policy.** Eligibility thresholds, rates and contact rules are placeholders, not real lending or regulatory policy.
- **Cost and latency.** One customer message can trigger several model calls (supervisor, one or more specialists, compliance).
