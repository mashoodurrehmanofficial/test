# Generated by Django 3.0.8 on 2020-07-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0016_auto_20200707_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
