from datetime import timedelta

from django import template
from django.utils import timezone

from cards.models import Card

register = template.Library()


@register.simple_tag
def card_for_studying():
    one_hour_ago = timezone.now() - timedelta(minutes=1)
    return Card.objects.filter(is_active=True, updated_at__lt=one_hour_ago).count()
