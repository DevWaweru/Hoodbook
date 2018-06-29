from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as authviews

urlpatterns = [
    url('^$',views.home, name='home'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)