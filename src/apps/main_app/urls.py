from django.conf.urls import url
# from django.contrib import admin
from .views import (
    home,
    detail,
    post_treasure,
)


urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'([0-9]+)/$', detail, name='detail'),
    url(r'^post_url/$', post_treasure, name='post_treasure')
]
