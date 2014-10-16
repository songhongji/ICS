from django.conf.urls import patterns, include, url

from django.contrib import admin
#admin.autodiscover()

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
     url(r'^xadmin/', include(xadmin.site.urls))
)
