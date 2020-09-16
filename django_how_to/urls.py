from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index, name='django-how-to'), 
    path('<str:url>', fetchpost, name='fetchpost'), 
    path('test/post/<str:ip>/<slug:title>/', testfetchpostusingip, name='testfetchpostusingip')
]
