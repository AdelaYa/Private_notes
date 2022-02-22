from django.urls import path

from . import views


urlpatterns = [
    path('note/list/', views.NoteListView.as_view(), name='index'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]