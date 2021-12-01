from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

import datetime

from .forms import GuestChatForm
from .models import ChatMessage
from .utils import DataMixin


class HomePage(ListView):
    model = ChatMessage
    template_name = 'testapp/index.html'
    context_object_name = 'entries'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django'
        context['description'] = 'Запуск приложения на Django!'

        return context


# Домашняя страничка
# def index(request):
#     entries = ChatMessage.objects.order_by('-create_date').all()
#
#     paginator = Paginator(entries, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'title': 'Django',
#         'description': 'Запуск приложения на Django!',
#         'page_obj': page_obj,
#     }
#     return render(request, 'testapp/index.html', context)


def get_json_view(request):
    data = {
        'received_headers': dict(request.headers.items()),
        'client_cookies': request.COOKIES,
        'url': request.path
    }
    return JsonResponse(data)


# @require_http_methods(['GET'])
# def get_some_view(request):
#     context = {
#         'title': 'Информация о пользователе',
#         'path': request.path,
#         'received_headers': request.headers.items(),
#         'client_cookies': request.COOKIES
#     }
#     return render(request, 'testapp/get_information.html', context)


class SomeView(LoginRequiredMixin, ListView):
    template_name = 'testapp/get_information.html'
    login_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.path = request.path
        self.received_headers = request.headers.items()
        self.client_cookies = request.COOKIES
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о пользователе'
        context['description'] = 'Запуск приложения на Django!'
        context['path'] = self.path
        context['received_headers'] = self.received_headers
        context['client_cookies'] = self.client_cookies
        return context

    def get_queryset(self):
        pass


class GuestChatView(DataMixin, CreateView):
    form_class = GuestChatForm
    template_name = 'testapp/guest_chat.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        data_cont = self.get_page_inf(title='Chat!')
        return context | data_cont


# @require_http_methods(['GET', 'POST'])
# @csrf_exempt
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
