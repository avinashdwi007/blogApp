
from django.urls import path

from blogApp import views


urlpatterns = [
    path('blog', views.blog,name='blog'),
]
