from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about')
]