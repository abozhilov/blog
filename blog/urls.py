from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('articles.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
