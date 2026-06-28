from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('booking/',booking,name='booking'),
    path('history/',history,name='history'),
    path('profile/',profile,name='profile'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('book/<int:id>/',book,name='book'),
    path('update/<int:id>',update,name='update'),
    path('clear/<int:id>/',clear,name='clear'),
    path('success/',success,name='success')
]