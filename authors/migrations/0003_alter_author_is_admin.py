# Generated by Django 4.1.2 on 2022-10-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_remove_author_host_remove_author_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
