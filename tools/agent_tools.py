
from tools.customer_tools import find_customer

from tools.payment_reminder_tools import (
    get_customer_account,
    get_payment_history
)

from tools.negotiation_tools import (
    get_repayment_options,
    check_repayment_eligibility,
    calculate_installment
)

from tools.hardship_tools import (
    get_hardship_programs,
    check_hardship_eligibility,
    submit_hardship_request
)

from tools.dispute_tools import (
    get_transaction_history,
    get_transaction_details,
    create_dispute_case,
    get_dispute_status
)

from tools.payment_processing_tools import (
    get_payment_methods,
    validate_payment_request,
    initiate_payment,
    get_payment_status
)

from tools.compliance_tools import (
    get_collection_policy,
    get_contact_restrictions,
    get_repayment_policy,
    get_disclosure_requirements,
    record_compliance_audit
)

from tools.escalation_tools import (
    get_escalation_queue,
    create_escalation_case,
    get_escalation_status,
    add_escalation_note
)

SUPERVISOR_TOOLS = [
    find_customer
]

PAYMENT_REMINDER_TOOLS = [
    get_customer_account,
    get_payment_history
]

PAYMENT_NEGOTIATION_TOOLS = [
    get_customer_account,
    get_repayment_options,
    check_repayment_eligibility,
    calculate_installment
]

FINANCIAL_ASSISTANCE_TOOLS = [
    get_customer_account,
    get_hardship_programs,
    check_hardship_eligibility,
    submit_hardship_request
]

DISPUTE_RESOLUTION_TOOLS = [
    get_transaction_history,
    get_transaction_details,
    create_dispute_case,
    get_dispute_status
]

PAYMENT_PROCESSING_TOOLS = [
    get_payment_methods,
    validate_payment_request,
    initiate_payment,
    get_payment_status
]

COMPLIANCE_TOOLS = [
    get_collection_policy,
    get_contact_restrictions,
    get_repayment_policy,
    get_disclosure_requirements,
    record_compliance_audit
]

HUMAN_ESCALATION_TOOLS = [
    get_escalation_queue,
    create_escalation_case,
    get_escalation_status,
    add_escalation_note
]