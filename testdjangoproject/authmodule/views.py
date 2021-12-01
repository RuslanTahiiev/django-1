from django.urls import reverse_lazy
from django.views.generic import CreateView

from authmodule.forms import SignUpUserForm


class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(SignUpUser, self).get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context
