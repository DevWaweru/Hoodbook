from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as authviews

urlpatterns = [
    url('^$',views.home, name='home'),
]