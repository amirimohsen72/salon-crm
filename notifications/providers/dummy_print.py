# notifications/providers/dummy.py

class DummySMSProvider:
    """
    Provider تستی – هیچ پیامکی ارسال نمی‌کند
    """

    def send(self, phone_number: str, message: str) -> str:
        print("==== DUMMY SMS ====")
        print("To:", phone_number)
        print("Message:", message)
        print("===================")
        return "DUMMY_OK"