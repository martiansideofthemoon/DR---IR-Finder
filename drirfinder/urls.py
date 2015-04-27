<<<<<<< HEAD
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'drirfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
=======
from django.conf.urls import patterns, url
from drirfinder import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
>>>>>>> e34d721d43c41fa1deb6930ebc2c5fcc40766145
