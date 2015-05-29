from django import forms
from cloudinary.forms import CloudinaryJsFileField

from thimble.apps.Portfolios.models.schemas.Collection import Collection

class CreateCollection(forms.ModelForm):
	photos = CloudinaryJsFileField(attrs={'multiple': 1}, required=True)
	class Meta:
		model   = Collection
		fields  = ("title", "description")
		widgets = {
		    'description': forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class':'form-control', 
		                                         'placeholder':'Tell the story of the collection'}),

		    'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Your Collection', 'required':True})
		}
