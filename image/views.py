#!/usr/bin/env python
# -*- coding: latin-1 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect

from image.models import Images, Pics, Photos
from image.forms import ImageForm, PicForm, PhotoForm

def index(request):
	imgs = Images.objects.all()
	pics = Pics.objects.all()
	photos = Photos.objects.all()
	return render(request, 'image/index.html',{'imgs':imgs,'pics':pics,'photos':photos})

def formulario(request):
	#print "oaaa" <-- this save me ... ¬¬
	#ue=False "usuario_existe":ue,
	if request.method == 'POST': # If the form has been submitted...
		form = ImageForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			
			nombre = form.cleaned_data['nombre']
			imagen = form.cleaned_data['imagen']
			i = Images(nombre=nombre,imagen=imagen)
			i.save()
			
			return HttpResponseRedirect('/image/thanks/')
			
	else:
		form = ImageForm()
	return render(request, 'image/form.html', {
		'form': form,
	})
def formulario2(request):
	#print "oaaa" <-- this save me ... ¬¬
	#ue=False "usuario_existe":ue,
	if request.method == 'POST': # If the form has been submitted...
		form = PicForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			
			nombre = form.cleaned_data['nombre']
			imagen = form.cleaned_data['imagen']
			p = Pics(nombre=nombre,imagen=imagen)
			p.save()
			
			return HttpResponseRedirect('/image/thanks/')
			
	else:
		form = PicForm()
	return render(request, 'image/form.html', {
		'form': form,
	})

def formulario3(request):
	#print "oaaa" <-- this save me ... ¬¬
	#ue=False "usuario_existe":ue,
	if request.method == 'POST': # If the form has been submitted...
		form = PhotoForm(request.POST, request.FILES) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			
			nombre = form.cleaned_data['nombre']
			imagen = form.cleaned_data['imagen']
			p = Photos(nombre=nombre,imagen=imagen)
			p.save()
			
			return HttpResponseRedirect('/image/thanks/')
			
	else:
		form = PhotoForm()
	return render(request, 'image/form.html', {
		'form': form,
	})

def thanks(request):
	return render(request, 'image/thanks.html')
