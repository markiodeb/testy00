from django.conf.urls import patterns, include, url

from image import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^formulario/$', views.formulario, name='formulario'),
	url(r'^thanks/$', views.thanks, name='thanks'),
	url(r'^formulario2/$', views.formulario2, name='formulario2'),
	url(r'^formulario3/$', views.formulario3, name='formulario3'),
)
