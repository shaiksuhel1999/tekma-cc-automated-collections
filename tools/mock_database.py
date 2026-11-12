"""
In-memory mock data for the Credit Card Collections system.

Everything here is illustrative development data. The customers are
chosen so that every branch of the tools can be exercised:

    CUST-1001  John Smith    35 days overdue   hardship + EMI eligible
    CUST-1002  Priya Sharma  current           nothing overdue
    CUST-1003  Rahul Verma   12 days overdue   EMI eligible, hardship not yet
    CUST-1004  Anita Desai   65 days overdue   hardship + EMI, vulnerable flag
    CUST-1005  Vikram Nair   120 days overdue  EMI ineligible, contact restricted
    CUST-1006  Meera Iyer    40 days overdue   balance too low for EMI

`days_overdue` is stored (not computed) and is consistent with
`due_date` as of AS_OF_DATE.
"""

import re
from uuid import uuid4

AS_OF_DATE = "2026-11-09"

CUSTOMERS = {
    "CUST-1001": {
        "customer_id": "CUST-1001",
        "name": "Johnn Smith",
        "phone": "+91-98765-01001",
        "email": "johnn.smith@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-1234",
        "card_last4": "1234",
        "outstanding_balance": 45000.00,
        "minimum_due": 5000.00,
        "days_overdue": 35,
        "payment_status": "OVERDUE",
        "due_date": "2026-10-05",
        "credit_limit": 100000.00,
        "currency": "INR"
    },
    "CUST-1002": {
        "customer_id": "CUST-1002",
        "name": "Jriya Sharma",
        "phone": "+91-98765-01002",
        "email": "jriya.sharma@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-5678",
        "card_last4": "5678",
        "outstanding_balance": 18500.00,
        "minimum_due": 925.00,
        "days_overdue": 0,
        "payment_status": "CURRENT",
        "due_date": "2026-11-20",
        "credit_limit": 150000.00,
        "currency": "INR"
    },
    "CUST-1003": {
        "customer_id": "CUST-1003",
        "name": "Yahul Verma",
        "phone": "+91-98765-01003",
        "email": "yahul.verma@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-9012",
        "card_last4": "9012",
        "outstanding_balance": 27800.00,
        "minimum_due": 2780.00,
        "days_overdue": 12,
        "payment_status": "OVERDUE",
        "due_date": "2026-10-28",
        "credit_limit": 80000.00,
        "currency": "INR"
    },
    "CUST-1004": {
        "customer_id": "CUST-1004",
        "name": "Gnita Desai",
        "phone": "+91-98765-01004",
        "email": "gnita.desai@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-3456",
        "card_last4": "3456",
        "outstanding_balance": 132000.00,
        "minimum_due": 13200.00,
        "days_overdue": 65,
        "payment_status": "OVERDUE",
        "due_date": "2026-09-05",
        "credit_limit": 200000.00,
        "currency": "INR"
    },
    "CUST-1005": {
        "customer_id": "CUST-1005",
        "name": "Sikram Nair",
        "phone": "+91-98765-01005",
        "email": "sikram.nair@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-7890",
        "card_last4": "7890",
        "outstanding_balance": 88000.00,
        "minimum_due": 22000.00,
        "days_overdue": 120,
        "payment_status": "DELINQUENT",
        "due_date": "2026-07-12",
        "credit_limit": 90000.00,
        "currency": "INR"
    },
    "CUST-1006": {
        "customer_id": "CUST-1006",
        "name": "Keera Iyer",
        "phone": "+91-98765-01006",
        "email": "keera.iyer@example.com",
        "card_number_masked": "XXXX-XXXX-XXXX-2468",
        "card_last4": "2468",
        "outstanding_balance": 3200.00,
        "minimum_due": 500.00,
        "days_overdue": 40,
        "payment_status": "OVERDUE",
        "due_date": "2026-09-30",
        "credit_limit": 50000.00,
        "currency": "INR"
    }
}

PAYMENT_HISTORY = {
    "CUST-1001": [
        {
            "payment_id": "PAY-001",
            "amount": 10000.00,
            "status": "SUCCESS",
            "date": "2026-09-01"
        }
    ],
    "CUST-1002": [
        {
            "payment_id": "PAY-002",
            "amount": 22000.00,
            "status": "SUCCESS",
            "date": "2026-09-18"
        },
        {
            "payment_id": "PAY-003",
            "amount": 15400.00,
            "status": "SUCCESS",
            "date": "2026-10-19"
        }
    ],
    "CUST-1003": [
        {
            "payment_id": "PAY-004",
            "amount": 6000.00,
            "status": "SUCCESS",
            "date": "2026-09-25"
        },
        {
            "payment_id": "PAY-005",
            "amount": 2780.00,
            "status": "FAILED",
            "date": "2026-10-27"
        }
    ],
    "CUST-1004": [
        {
            "payment_id": "PAY-006",
            "amount": 12000.00,
            "status": "SUCCESS",
            "date": "2026-08-02"
        },
        {
            "payment_id": "PAY-007",
            "amount": 13200.00,
            "status": "FAILED",
            "date": "2026-09-04"
        }
    ],
    "CUST-1005": [
        {
            "payment_id": "PAY-008",
            "amount": 5000.00,
            "status": "SUCCESS",
            "date": "2026-06-10"
        }
    ],
    "CUST-1006": [
        {
            "payment_id": "PAY-009",
            "amount": 1500.00,
            "status": "SUCCESS",
            "date": "2026-08-28"
        },
        {
            "payment_id": "PAY-010",
            "amount": 500.00,
            "status": "PENDING",
            "date": "2026-11-08"
        }
    ]
}

TRANSACTIONS = {
    "CUST-1001": [
        {
            "transaction_id": "TXN-1001",
            "merchant": "ABC Electronics",
            "amount": 12000.00,
            "date": "2026-10-15",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-1002",
            "merchant": "XYZ Stores",
            "amount": 5000.00,
            "date": "2026-10-18",
            "status": "POSTED",
            "type": "PURCHASE"
        }
    ],
    # TXN-2002 is an unrecognised merchant (UNKNOWN_MERCHANT dispute).
    "CUST-1002": [
        {
            "transaction_id": "TXN-2001",
            "merchant": "FreshMart Groceries",
            "amount": 3200.00,
            "date": "2026-10-22",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-2002",
            "merchant": "INTL*QK-PAY 8841",
            "amount": 9800.00,
            "date": "2026-10-27",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-2003",
            "merchant": "City Fuel Station",
            "amount": 5500.00,
            "date": "2026-11-02",
            "status": "POSTED",
            "type": "PURCHASE"
        }
    ],
    # TXN-3001 / TXN-3002 are a duplicate charge (DUPLICATE_TRANSACTION dispute).
    "CUST-1003": [
        {
            "transaction_id": "TXN-3001",
            "merchant": "SkyWings Airlines",
            "amount": 13900.00,
            "date": "2026-10-10",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-3002",
            "merchant": "SkyWings Airlines",
            "amount": 13900.00,
            "date": "2026-10-10",
            "status": "POSTED",
            "type": "PURCHASE"
        }
    ],
    "CUST-1004": [
        {
            "transaction_id": "TXN-4001",
            "merchant": "HomeStyle Furniture",
            "amount": 85000.00,
            "date": "2026-08-03",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-4002",
            "merchant": "Apollo Pharmacy",
            "amount": 6400.00,
            "date": "2026-08-12",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-4003",
            "merchant": "Late Payment Fee",
            "amount": 1200.00,
            "date": "2026-10-06",
            "status": "POSTED",
            "type": "FEE"
        }
    ],
    "CUST-1005": [
        {
            "transaction_id": "TXN-5001",
            "merchant": "Metro Wholesale",
            "amount": 42000.00,
            "date": "2026-06-18",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-5002",
            "merchant": "Late Payment Fee",
            "amount": 1300.00,
            "date": "2026-08-13",
            "status": "POSTED",
            "type": "FEE"
        },
        {
            "transaction_id": "TXN-5003",
            "merchant": "Late Payment Fee",
            "amount": 1300.00,
            "date": "2026-09-13",
            "status": "POSTED",
            "type": "FEE"
        }
    ],
    # TXN-6002 is a fee the customer may contest (INCORRECT_FEE dispute).
    "CUST-1006": [
        {
            "transaction_id": "TXN-6001",
            "merchant": "BookNest Online",
            "amount": 2400.00,
            "date": "2026-09-08",
            "status": "POSTED",
            "type": "PURCHASE"
        },
        {
            "transaction_id": "TXN-6002",
            "merchant": "Late Payment Fee",
            "amount": 800.00,
            "date": "2026-10-01",
            "status": "POSTED",
            "type": "FEE"
        }
    ]
}


REPAYMENT_PLANS = [
    {
        "plan_id": "EMI-3",
        "months": 3,
        "annual_interest_rate": 15.0,
        "available": True
    },
    {
        "plan_id": "EMI-6",
        "months": 6,
        "annual_interest_rate": 15.0,
        "available": True
    },
    {
        "plan_id": "EMI-12",
        "months": 12,
        "annual_interest_rate": 16.0,
        "available": True
    }
]


HARDSHIP_PROGRAMS = [
    {
        "program_id": "HARDSHIP-001",
        "name": "Temporary Financial Assistance",
        "description": "Review of repayment options for eligible customers.",
        "minimum_overdue_days": 30,
        "requires_review": True
    }
]


# Applied to every customer unless overridden below.
DEFAULT_CONTACT_RESTRICTIONS = {
    "contact_allowed": True,
    "restricted_channels": [],
    "preferred_channel": "PHONE",
    "daily_contact_limit": 1,
    "vulnerable_customer": False,
    "requires_policy_verification": True,
    "notes": ""
}

CONTACT_RESTRICTIONS = {
    "CUST-1004": {
        "vulnerable_customer": True,
        "notes": "Customer reported job loss. Handle under the hardship protocol."
    },
    "CUST-1005": {
        "restricted_channels": ["PHONE", "SMS"],
        "preferred_channel": "EMAIL",
        "notes": "Customer requested written communication only."
    }
}


DISPUTES = {}
ESCALATIONS = {}
PAYMENT_REQUESTS = {}
COMPLIANCE_AUDITS = {}
HARDSHIP_REQUESTS = {}


def generate_reference(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8].upper()}"


_CUSTOMER_ID_PATTERN = re.compile(r"^(?:CUST)?[\s\-_#]*(\d+)$")


def normalize_customer_id(customer_id) -> str:
    """
    Convert loosely typed customer IDs to the stored form.

    'cust-1001', ' CUST-1001 ', 'CUST1001' and '1001' all become
    'CUST-1001'. Anything else is returned trimmed and upper-cased,
    so an unknown value simply fails the lookup.
    """

    value = str(customer_id or "").strip().upper()
    match = _CUSTOMER_ID_PATTERN.match(value)

    return f"CUST-{match.group(1)}" if match else value


def find_customers(identifier: str) -> list[dict]:
    """
    Find customers by customer ID, full or partial name, email,
    phone number or the last four digits of the card.
    """

    raw = str(identifier or "").strip()

    if not raw:
        return []

    matches = {}

    candidate_id = normalize_customer_id(raw)
    if candidate_id in CUSTOMERS:
        matches[candidate_id] = CUSTOMERS[candidate_id]

    text = raw.lower()
    digits = re.sub(r"\D", "", raw)

    for customer_id, customer in CUSTOMERS.items():

        if text == customer["email"].lower():
            matches[customer_id] = customer

        if len(text) >= 3 and text in customer["name"].lower():
            matches[customer_id] = customer

        if digits:
            phone_digits = re.sub(r"\D", "", customer["phone"])

            if digits == customer["card_last4"]:
                matches[customer_id] = customer

            if len(digits) >= 10 and phone_digits.endswith(digits[-10:]):
                matches[customer_id] = customer

    return list(matches.values())


def get_contact_restrictions_for(customer_id: str) -> dict:
    """Default contact restrictions merged with any customer override."""

    return {
        "customer_id": customer_id,
        **DEFAULT_CONTACT_RESTRICTIONS,
        **CONTACT_RESTRICTIONS.get(customer_id, {})
    }
