from django.conf.urls import url
from django.conf import settings
from testapp import views
from django.conf.urls.static import static

app_name = 'testapp'

'''
from django.conf.urls.static import static
'''
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fio/$', views.fio, name='fio'),
    url(r'^(?P<user_id>\d+)/(?P<question_id>\d+)/$', views.detail0, name='detail0'),
	url(r'^(?P<user_id>\d+)/(?P<question_id>\d+)/next/$', views.detail, name='detail'),
	url(r'^(?P<user_id>\d+)/down/$', views.download_file, name='down'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

'''
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
]

'''
'''



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''