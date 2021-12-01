from .models import ChatMessage


class DataMixin:
    def get_page_inf(self, **kwargs):
        context = kwargs
        context['entries'] = ChatMessage.objects.order_by('-create_date').all()

        return context
