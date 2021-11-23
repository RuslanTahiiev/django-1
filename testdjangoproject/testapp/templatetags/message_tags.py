from django import template
from ..models import Message

register = template.Library()


@register.simple_tag(name='getmessages')
def get_messages():
    return Message.objects.all()


@register.inclusion_tag('testapp/get_messages.html')
def show_messages():
    messages = Message.objects.all()
    context = {
        'messages': messages
    }
    return context