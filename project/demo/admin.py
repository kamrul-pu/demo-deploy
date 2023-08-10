from django.contrib import admin
from demo.models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )


admin.site.register(Note, NoteAdmin)
