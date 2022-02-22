from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Note
from .forms import NoteForm


class NoteListView(ListView):
    model = Note
    template_name = 'index.html'



class NoteUpdateView(UpdateView):
    model = Note
    fields = ['text']
    template_name = 'note_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('index')


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

