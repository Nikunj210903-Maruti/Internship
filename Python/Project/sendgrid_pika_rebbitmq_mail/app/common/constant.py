from enum import Enum


class QueueEnum(Enum):
    SEND_EMAIL = {'route': 'send_email', 'queue': 'send_email_q', 'worker_count': 1}
    UNSEND_EMAIL = {'route': 'unsend_email', 'queue': 'unsend_email_q', 'worker_count': 1}
