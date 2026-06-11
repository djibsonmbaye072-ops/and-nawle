from django.db import models
from core.models import BaseModel


class News(BaseModel):

    title = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to="news/"
    )

    content = models.TextField()

    published_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title