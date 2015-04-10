from django.conf.urls import patterns, include, url
from django.conf import settings
import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.jua_login, name='jua_login'),
    url(r'^sysadmin/', include('sysadmin.urls', namespace='sysadmin')),
    url(r'^usermanage/', include('usermanage.urls', namespace='usermanage')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
    	 settings.STATIC_ROOT, 'show_indexes': False}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
)
