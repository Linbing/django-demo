from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', 'learn.views.index',name='index'),
    url(r'^home/$', 'learn.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
