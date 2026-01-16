from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_test_email

@api_view(["POST"])
def trigger_email(request):
    email = request.data.get("email")
    send_test_email.delay(email)
    return Response({"message": "Email task triggered"})
