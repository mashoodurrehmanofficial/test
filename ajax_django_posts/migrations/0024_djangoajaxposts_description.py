# Generated by Django 3.0.8 on 2020-07-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0023_remove_djangoajaxposts_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoajaxposts',
            name='description',
            field=models.TextField(default='Here description will be place !'),
        ),
    ]
