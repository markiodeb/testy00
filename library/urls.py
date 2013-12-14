from django.conf.urls import patterns, include, url

from library import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^formulario_readbook/$', views.formulario_readbook, name='formulario_readbook'),
	url(r'^get_genre_books/$', views.get_genre_books, name='get_genre_books'),
)
