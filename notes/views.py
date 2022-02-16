from django.shortcuts import render
from django.views.generic import ListView


from . models import Note
from .forms import NoteForm


class NoteListView(ListView):
    model = Note
    template_name = 'index.html'


def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return render(request, 'index.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'note_new.html', {'form': form})
