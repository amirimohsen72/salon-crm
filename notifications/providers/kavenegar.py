import requests
from django.conf import settings


class KavenegarSMSProvider:
    """
    Provider ارسال پیامک (قابل تعویض)
    """

    def __init__(self):
        self.api_key = settings.SMS_API_KEY
        self.base_url = settings.SMS_BASE_URL
        self.sender = settings.SMS_SENDER_NUMBER

    def send(self, phone_number: str, message: str) -> str:
        payload = {
            'receptor': phone_number,
            'sender': self.sender,
            'message': message,
            'api': self.api_key,
        }

        response = requests.post(
            self.base_url,
            data=payload,
            timeout=10
        )

        response.raise_for_status()
        return response.text
