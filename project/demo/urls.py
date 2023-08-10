from django.urls import path

from demo.views import (
    NoteList,
    NoteDetail,
)


urlpatterns = [
    path("", NoteList.as_view(), name="note-list"),
    path("/<int:pk>", NoteDetail.as_view(), name="note-detail"),
]
