from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^image/', include('image.urls', namespace='image')),
	url(r'^library/', include('library.urls', namespace='library')),
    # Examples:
    # url(r'^$', 'testy.views.home', name='home'),
    # url(r'^testy/', include('testy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
