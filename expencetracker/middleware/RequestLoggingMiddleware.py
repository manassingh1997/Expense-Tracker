


from tracker.models import RequestLogs
from typing import Any


class RequestLogging:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        request_info = (request)
        
        RequestLogs.objects.create(
            request_info = vars(request_info),
            request_type = request_info.method,
            request_method = request_info.path
        )
        

        return self.get_response(request)