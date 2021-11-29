from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import ListView, CreateView

import datetime

from .forms import GuestChatForm
from .models import ChatMessage


class HomePage(ListView):
    model = ChatMessage
    template_name = 'testapp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django'
        context['description'] = 'Запуск приложения на Django!'

        return context



# Домашняя страничка
# def index(request):
#     context = {
#         'title': 'Django',
#         'description': 'Запуск приложения на Django!'
#     }
#     return render(request, 'testapp/index.html', context)


def get_json_view(request):
    data = {
        'received_headers': dict(request.headers.items()),
        'client_cookies': request.COOKIES,
        'url': request.path
    }
    return JsonResponse(data)


@require_http_methods(['GET'])
def get_some_view(request):
    context = {
        'title': 'Информация о пользователе',
        'path': request.path,
        'received_headers': request.headers.items(),
        'client_cookies': request.COOKIES
    }
    return render(request, 'testapp/get_information.html', context)


class GuestChatView(CreateView):
    form_class = GuestChatForm
    template_name = 'testapp/guest_chat.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Chat!'
        context['entries'] = ChatMessage.objects.order_by('-create_date').all()
        return context


@require_http_methods(['GET', 'POST'])
@csrf_exempt
# def guest_chat_view(request):
#     if request.method == 'POST':
#         form = GuestChatForm(request.POST)
#         if form.is_valid():
#             # obj = ChatMessage.objects.create(
#             #     **form.cleaned_data,
#             #     create_date=datetime.datetime.now(),
#             # )
#             # obj.save()
#             form.save()
#             messages.success(request, 'Отправлено!')
#             return redirect(reverse('chat'))
#     else:
#         form = GuestChatForm()
#     author_name = request.GET.get('name', None)
#     if author_name:
#         context = {
#             'title': 'Гостевой чатик!',
#             'form': form,
#             'path': request.path,
#             'entries': ChatMessage.objects.filter(name=author_name)
#         }
#     else:
#         context = {
#             'title': 'Гостевой чатик!',
#             'form': form,
#             'path': request.path,
#             'entries': ChatMessage.objects.order_by('-create_date').all()
#         }
#     return render(request, 'testapp/guest_chat.html', context)


@require_http_methods(['GET'])
def get_message_view(request, message_id):
    message = get_object_or_404(ChatMessage, id=message_id)
    context = {
        'message': message,
    }
    return render(request, 'testapp/message.html', context)


@require_http_methods(['GET'])
def get_author_view(request, message_slug):
    author_messages = ChatMessage.objects.filter(slug=message_slug).all()
    context = {
        'messages': author_messages,
    }
    return render(request, 'testapp/messages.html', context)
