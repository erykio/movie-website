from django.conf.urls import url
from . import views

app_name = 'charts'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]