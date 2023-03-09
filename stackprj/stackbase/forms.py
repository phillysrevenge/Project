from .models import Answer
from django import forms


class AnswerForm(forms.ModelForm):
    # class meta because we want to access some fields
    class Meta:
        model = Answer
        fields = ['name', 'content']
        # widget for addimg form control like normal html and css
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
