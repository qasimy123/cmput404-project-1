# Generated by Django 4.1.2 on 2022-10-20 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='host',
        ),
        migrations.RemoveField(
            model_name='author',
            name='url',
        ),
    ]
