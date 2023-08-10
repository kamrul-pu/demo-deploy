from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from demo.serializers import NoteListSerializer, NoteDetailSerializer

from demo.models import Note


class NoteList(ListCreateAPIView):
    serializer_class = NoteListSerializer
    queryset = Note.objects.filter()


class NoteDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.filter()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == "DELETE":
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (AllowAny,)
        return super().get_permissions()
