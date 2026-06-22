from django.db import models


class Leader(models.Model):

    full_name = models.CharField(
        max_length=255
    )

    title = models.CharField(
        max_length=255
    )

    photo = models.ImageField(
        upload_to="leaders/"
    )

    biography = models.TextField()

    vision = models.TextField()

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name