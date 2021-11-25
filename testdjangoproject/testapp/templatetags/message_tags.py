from django import template
from ..models import ChatMessage

register = template.Library()


@register.simple_tag(name='getmessages')
def get_messages():
    return ChatMessage.objects.all()


@register.inclusion_tag('testapp/get_messages.html')
def show_messages():
    messages = ChatMessage.objects.all()
    context = {
        'messages': messages
    }
    return context