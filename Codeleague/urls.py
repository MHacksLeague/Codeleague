from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(main.views.index)),
    url(r'^admin/', include(admin.site.urls)),
)
