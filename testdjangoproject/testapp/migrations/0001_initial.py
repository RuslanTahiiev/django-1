# Generated by Django 3.2.9 on 2021-11-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('create_date', models.DateTimeField(default='a', verbose_name='DATE')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'GuestChat',
                'verbose_name_plural': 'GuestChat',
                'ordering': ['name', '-create_date'],
            },
        ),
    ]
