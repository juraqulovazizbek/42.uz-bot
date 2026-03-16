from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .bot import handle_update, set_webhook
from .serializers import WebhookSerializer


class HandlerUpdateView(APIView):
    def post(self, request: Request) -> Response:
        # Here you would handle the incoming update from Telegram
        # For now, we just return a simple response
        update_data = request.data
        
        print("Received update:", update_data) 

        handle_update(update_data)

        return Response({"message": "Update received"}, status=status.HTTP_200_OK)
    
class SetWebhookView(APIView):
    def post(self, request: Request) -> Response:
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            webhook_url = serializer.validated_data['webhook_url']
            set_webhook(webhook_url)    

            return Response({"message": "Webhook set"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)