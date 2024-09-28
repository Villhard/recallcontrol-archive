from django import template

from cards.models import Card

register = template.Library()


@register.simple_tag
def card_for_studying():
    return Card.study_objects.count()
