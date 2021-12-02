from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authmodule.forms import SignUpUserForm, LoginUserForm


class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(SignUpUser, self).get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'signin.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data()
        context['title'] = 'Sign In'

        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('signin')
