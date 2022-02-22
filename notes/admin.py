from django.contrib import admin

from .models import Note
from django_summernote.admin import SummernoteModelAdmin


class NoteModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Note, NoteModelAdmin)


