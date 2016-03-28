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