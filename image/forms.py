from django.forms import ModelForm
from image.models import Images, Pics, Photos

class ImageForm(ModelForm):
	class Meta:
		model = Images

class PicForm(ModelForm):
	class Meta:
		model = Pics

class PhotoForm(ModelForm):
	class Meta:
		model = Photos
