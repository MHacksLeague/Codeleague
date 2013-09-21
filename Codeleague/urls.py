from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/andrei/Prog/hackathon/Codeleague'}),
	url(r'^profile/?', 'rank.views.HackerProfile'),
    url(r'^ranking/?', 'rank.views.Ranking'),
    url(r'^', 'main.views.index'),
    url(r'^admin/', include(admin.site.urls)),

)
