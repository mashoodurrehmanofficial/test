from django.contrib import admin
from .models import *
from django.apps import apps

app = apps.get_app_config('ajax_django_posts')
for model_name,model in app.models.items():
    admin.site.register(model)