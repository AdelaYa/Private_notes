from django.urls import path

from . import views


urlpatterns = [
    path('note/list/', views.NoteListView.as_view(), name='index'),
    path('note/new/', views.note_new, name='note_new'),
]