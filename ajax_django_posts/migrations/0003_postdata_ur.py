# Generated by Django 2.2 on 2020-07-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_django_posts', '0002_auto_20200706_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdata',
            name='ur',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
