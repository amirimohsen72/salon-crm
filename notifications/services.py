from django.utils import timezone
from django.conf import settings
from .models import SMSTemplate, SMSLog
from .providers.dummy_print import DummySMSProvider

def get_sms_provider():
    if settings.SMS_PROVIDER == 'kavenegar':
        from .providers.kavenegar import KavenegarSMSProvider
        return KavenegarSMSProvider()
    return DummySMSProvider()

def render_message(template_text: str, context: dict) -> str:
    for key, value in context.items():
        template_text = template_text.replace(f"{{{{{key}}}}}", str(value))
    return template_text


def send_sms(
    *,
    phone_number: str,
    template_type: str,
    context: dict,
    customer=None,
    appointment=None
):

    template = SMSTemplate.objects.filter(
        type=template_type,
        is_active=True
    ).first()

    if not template:
        return None

    message = render_message(template.message, context)

    sms_log = SMSLog.objects.create(
        template=template,
        customer=customer,
        appointment=appointment,
        phone_number=phone_number,
        message=message,
        status=SMSLog.Status.PENDING
    )
    provider = get_sms_provider()

    try:
        response = provider.send(phone_number, message)
        sms_log.status = SMSLog.Status.SENT
        sms_log.sent_at = timezone.now()
        sms_log.provider_response = response

    except Exception as e:
        sms_log.status = SMSLog.Status.FAILED
        sms_log.provider_response = str(e)

    sms_log.save()
    return sms_log
