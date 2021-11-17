from django.db import models
from datetime import datetime

from django.urls import reverse


class Message(models.Model):
    class Meta:
        pass

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(default=datetime.now())

    def __repr__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('message_inf', kwargs={'message_id': self.id})

