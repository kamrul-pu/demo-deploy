from rest_framework import serializers

from demo.models import Note


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            "id",
            "title",
            "description",
        )
        read_only_fields = ("id",)


class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            "title",
            "description",
            "created_at",
            "updated_at",
        )
