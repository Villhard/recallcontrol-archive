from django import template

from cards.models import Card

register = template.Library()


@register.simple_tag(takes_context=True)
def card_for_studying(context):
    user = context["request"].user
    if user.is_authenticated:
        return Card.study_objects.filter(owner=user).count()
