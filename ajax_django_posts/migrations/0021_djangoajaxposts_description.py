# Generated by Django 3.0.8 on 2020-07-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0020_auto_20200709_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoajaxposts',
            name='description',
            field=models.TextField(default='Coming Soon !'),
        ),
    ]
