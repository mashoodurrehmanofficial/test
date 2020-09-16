from django.contrib import admin

# Register your models here.
from .models import *
from django.apps import apps

app = apps.get_app_config('django_how_to').models.items()
for model_name,model in app:
    admin.site.register(model)