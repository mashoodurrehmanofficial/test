# Generated by Django 3.0.8 on 2020-07-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_how_to', '0003_djangohowtopost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangohowtopost',
            name='description',
            field=models.TextField(default='Here description will be place !'),
        ),
    ]
