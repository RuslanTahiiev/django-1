from django.db import models
from datetime import datetime


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    create_date = models.DateTimeField(default=datetime.now())

    def __repr__(self):
        return f'{self.name}'

