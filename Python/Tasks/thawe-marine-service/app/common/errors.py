__all__ = ['errors']

errors = {
    'BadRequestError': {
        'ok': False,
        'error': 'BAD_REQUEST',
        'message': "",
        'status': 400,
    },
    'InvalidEmailData': {
        'ok': False,
        'error': 'INVALID_EMAIL_DATA',
        'message': "",
        'status': 400,
    }
}
