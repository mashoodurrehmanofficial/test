from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index, name='django-ajax'),
    path('<str:url>', fetchpost, name='posts'),
    
    
    path('getcities/<str:country>', getcities, name='getcities'),
    path('verifyemail/<str:email>', verifyemail, name='verifyemail'),
    path('loadmore/', loadmore, name='loadmore'),
    path('getdata/<str:country_name>', getdata, name='getdata'),
    path('realtimeautocompletebox/<str:query>', realtimeautocompletebox, name='realtimeautocompletebox')
]
