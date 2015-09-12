from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lab.views.index', name='index'),
    url(r'^home/', 'lab.views.home', name='home'),
    url(r'^downloadrdp/$','lab.views.create_rdp_file'),
#    url(r'^logout/', 'lab.views.logout_view'),
#django_cas links
	url(r'^accounts/login/$', 'django_cas.views.login'),
	url(r'^accounts/logout/', 'django_cas.views.logout'),
#django_cas ends
#     url(r'^blog/', include('blog.urls')),
   url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
