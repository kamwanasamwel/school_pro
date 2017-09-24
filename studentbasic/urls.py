from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.primary_create, name='basic'),
]