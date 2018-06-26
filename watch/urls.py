from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('',include('hood.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]