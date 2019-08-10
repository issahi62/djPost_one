from django import forms 
from .models import Post, Author
 

class PostForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    contact = forms.FloatField(max_value=10) 
    image = forms.ImageField()
    slug = forms.SlugField(allow_unicode=False, required=False)



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image", "slug")
