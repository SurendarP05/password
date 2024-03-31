from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServerError(APIException):
    status_code = 500
    default_detail = ' Internal server error'
    default_code ='server_error'
