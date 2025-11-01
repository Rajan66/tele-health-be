import os
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from base.utils import generate_token as token04

ZEGO_APP_ID = int(os.getenv("ZEGO_APP_ID", 0))
ZEGO_SERVER_SECRET = os.getenv("ZEGO_SERVER_SECRET", "")
TOKEN_EXPIRY = int(os.getenv("ZEGO_TOKEN_EXPIRY", 3600))


class ZegoTokenAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user_id = str(user.id)
        payload = {"demoPayload": ""}

        token_info = token04.generate_token04(
            app_id=ZEGO_APP_ID,
            user_id=user_id,
            secret=ZEGO_SERVER_SECRET,
            effective_time_in_seconds=TOKEN_EXPIRY,
            payload=json.dumps(payload),
        )

        if token_info.error_code != 0:
            return Response(
                {
                    "error": token_info.error_message,
                    "error_code": token_info.error_code,
                },
                status=400,
            )

        return Response(
            {"token": token_info.token, "expires_in": TOKEN_EXPIRY}
        )
