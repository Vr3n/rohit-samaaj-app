import json
from django.utils.deprecation import MiddlewareMixin
from django.contrib.messages import get_messages
from django.http import HttpRequest, HttpResponse


class HtmxMessageMiddleware(MiddlewareMixin):
    """
    Middleware that moves messages into the HX-Trigger header when request is made with HTMX.
    """

    def process_response(
        self,
        request: HttpRequest,
        response: HttpResponse
    ) -> HttpResponse:

        # The Hx-Request header indicates that the request was made with HTMX.
        if "HX-Request" not in request.headers:
            return response

        # Ignore redirections because HTMX cannot read the headers.
        if 300 <= response.status_code < 400:
            return response

        # Extract the messages.
        messages = [
            {"message": message.message, "tags": message.tags}
            for message in get_messages(request)
        ]

        if not messages:
            return response

        # Get the existing HX-Trigger that could have been defined by the view.
        hx_trigger = response.headers.get("HX-Trigger")

        if hx_trigger is None:
            # If the HX-Trigger is not set, start with an empty set.
            hx_trigger = {}

        elif hx_trigger.startswith("{"):
            # if the HX-Trigger uses the object syntax, parse the object.
            hx_trigger = json.loads(hx_trigger)
        else:
            hx_trigger = {
                hx_trigger: True
            }

        # Add the messages array in the Hx-Trigger object.
        hx_trigger["messages"] = messages

        # Add or update the Hx-Trigger
        response.headers[
            "HX-Trigger"
        ] = json.dumps(hx_trigger)

        return response
