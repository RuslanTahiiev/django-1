from django import forms
from django.core.exceptions import ValidationError
# from django.forms import CharField, Textarea, IntegerField
from captcha.fields import CaptchaField

import datetime

from .models import ChatMessage

# class GuestChatForm(forms.Form):
#     name = CharField(
#         label='Ваше имя',
#         required=True,
#         strip=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         ),
#     )
#     message = CharField(
#         label='Оставьте сообщение:',
#         required=True,
#         min_length=5,
#         widget=Textarea(
#             attrs={
#                 'cols': '30',
#                 'rows': '5',
#                 'class': 'form-control'
#             }
#         ),
#
#     )


class GuestChatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].empty_label = 'Name'

    captcha = CaptchaField()

    class Meta:
        model = ChatMessage
        fields = ['name', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'cols': '30',
                'rows': '5',
                'class': 'form-control'
            }),
        }

    # Валидатор для поля имени (clean_ + [имя поля])
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('200 chars its max!')

        return name
