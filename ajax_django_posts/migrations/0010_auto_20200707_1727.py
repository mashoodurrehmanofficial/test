# Generated by Django 3.0.8 on 2020-07-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0009_auto_20200706_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='postdata',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
