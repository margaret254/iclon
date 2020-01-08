from django import forms

class PostForm(forms.Form):
    caption = forms.CharField(label='caption',max_length=100)
    image = forms.ImageField(label='Upload Image')