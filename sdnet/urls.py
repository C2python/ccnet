# -*- coding: utf-8 -*-

from django.urls import path
from sdnet import views

urlpatterns = [
    path('',views.fallback,name='fallback'),
    path('health/',views.health,name='health'),
]