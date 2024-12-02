import requests
from django.conf import settings

class Paystack:
    PAYSTACK_BASE_URL = "https://api.paystack.co"

    def __init__(self):
        self.secret_key = settings.PAYSTACK_SECRET_KEY

    def initialize_payment(self, email, amount):
        """Initialize a payment request"""
        url = f"{self.PAYSTACK_BASE_URL}/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "email": email,
            "amount": int(amount) * 100,  # Convert to kobo
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    def verify_payment(self, reference):
        """Verify a payment by reference"""
        url = f"{self.PAYSTACK_BASE_URL}/transaction/verify/{reference}"
        headers = {
            "Authorization": f"Bearer {self.secret_key}",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
