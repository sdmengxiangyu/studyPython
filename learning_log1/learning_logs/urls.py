from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index')
    # url(r'^$', views.index, name='index'),
]