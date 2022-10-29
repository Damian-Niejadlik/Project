from django import forms


class ImageForm(forms.ModelForm):
    date = forms.DateField()
    image = forms.ImageField()
    comment = forms.CharField(label='Your comment', max_length=16)