from django import forms
from .models import Note
from django_summernote.widgets import SummernoteWidget


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text',)
        widgets = {
            'text': SummernoteWidget()
        }


