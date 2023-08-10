from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Note"
        verbose_name_plural = "Notes"
