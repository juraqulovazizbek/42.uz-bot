from django.urls import path

from .views import HandlerUpdateView, SetWebhookView

urlpatterns = [
    path('webhook/', HandlerUpdateView.as_view(), name='handle_update'),
    path('set-webhook/', SetWebhookView.as_view(), name='set-webhook'),
]