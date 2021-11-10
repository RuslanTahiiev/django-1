from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import GuestChatForm
from .models import Message

# Домашняя страничка
def index(request):
    context = {
        'title': 'Django',
        'description': 'Запуск первого приложения на Django!'
    }
    return render(request, 'testapp/index.html', context)


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


@require_http_methods(['GET', 'POST'])
@csrf_exempt
def guest_chat_view(request):
    if request.method == 'POST':
        form = GuestChatForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data.get('name'),
                message=form.cleaned_data.get('message')
            )
            messages.success(request, 'Отправлено!')
            return HttpResponseRedirect('chat')
    else:
        form = GuestChatForm()
    context = {
        'title': 'Гостевой чатик!',
        'form': form,
        'path': request.path,
        'entries': Message.objects.all()
    }
    return render(request, 'testapp/guest_chat.html', context)
