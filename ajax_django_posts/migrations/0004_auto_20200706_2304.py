# Generated by Django 2.2 on 2020-07-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0003_postdata_ur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='ur',
            field=models.CharField(blank=True, default='s', max_length=100),
        ),
    ]
