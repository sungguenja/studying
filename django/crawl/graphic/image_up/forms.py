from django import forms
from .models import Post

class PetFormModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False