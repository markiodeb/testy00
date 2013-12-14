from django.forms import ModelForm
from library.models import ReadBook

class ReadBookForm(ModelForm):
	class Meta:
		model = ReadBook
