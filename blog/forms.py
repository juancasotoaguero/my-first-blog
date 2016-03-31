from django import forms
from models import Post
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {
            'title': _('Titulo'),
            'text': _('Contenido'),
                  } 

class Contact_form(forms.Form):
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)
    emisor = forms.EmailField()
    cc = forms.BooleanField(required = False)
    