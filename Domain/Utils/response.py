class response:
    data = None
    message = None
    success = None

    def __init__(self, data=None, message="", success=False):
        self.data = data
        self.message = message
        self.success = success


def json_response(data=None, success=None, message=''):
    return {
        'data': data,
        'success': success,
        'message': message
    }


def json_error_response(e):
    exception_message = 'Ocurrió un error: ' + str(e)
    return json_response(success=False, message=exception_message)
