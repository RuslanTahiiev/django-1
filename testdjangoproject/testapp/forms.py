from django import forms
from django.forms import CharField, Textarea, IntegerField


class GuestChatForm(forms.Form):
    name = CharField(
        label='Ваше имя',
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
    message = CharField(
        label='Оставьте сообщение:',
        required=True,
        min_length=5,
        widget=Textarea(
            attrs={
                'cols': '30',
                'rows': '5',
                'class': 'form-control'
            }
        ),

    )
