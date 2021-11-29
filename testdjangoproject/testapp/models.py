import datetime

from django.db import models

from django.urls import reverse
from django.utils.text import slugify


class ChatMessage(models.Model):
    class Meta:
        verbose_name = 'GuestChat'
        verbose_name_plural = 'GuestChat'
        ordering = ['name', '-create_date']

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(default=None, verbose_name='DATE')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+str(self.id))
        self.create_date = datetime.datetime.now()
        super(ChatMessage, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('message_inf', kwargs={'message_id': self.id})

