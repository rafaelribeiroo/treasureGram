from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from .views import (
    home,
    detail,
    post_treasure,
    profile,
    login_view
)


urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'([0-9]+)/$', detail, name='detail'),
    url(r'^post_url/$', post_treasure, name='post_treasure'),
    url(r'^login/$', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
