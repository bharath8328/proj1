from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('persons/',persons,name='persons'),
    path('login/',login),
    path('thankyou/',thankyou),
]
