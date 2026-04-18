from django.utils import timezone
from datetime import timedelta
from .models import ContactMessage

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def is_spam(request):
    ip = get_client_ip(request)
    one_minute_ago = timezone.now() - timedelta(minutes=1)

    return ContactMessage.objects.filter(
        ip_address=ip,
        created_at__gte=one_minute_ago
    ).exists()