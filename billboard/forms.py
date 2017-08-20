from django import forms
from .models import Entry


class newEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'message', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Your message here'}),
            'author': forms.TextInput   (
                attrs={'placeholder': 'Author'}),
        }