from django.db import models
from core.models import BaseModel


class News(BaseModel):

    title = models.CharField(
        max_length=255,
        verbose_name="Titre"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug"
    )

    cover_image = models.ImageField(
        upload_to="news/covers/",
        blank=True,
        null=True,
        verbose_name="Image de couverture"
    )

    excerpt = models.TextField(
        blank=True,
        verbose_name="Résumé"
    )

    content = models.TextField(
        verbose_name="Contenu"
    )

    document = models.FileField(
        upload_to="news/documents/",
        blank=True,
        null=True,
        verbose_name="Document PDF"
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Publié"
    )

    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de publication"
    )

    class Meta:
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class NewsImage(models.Model):

    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="gallery",
        verbose_name="Actualité"
    )

    image = models.ImageField(
        upload_to="news/gallery/",
        verbose_name="Image"
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Légende"
    )

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Galerie Photos"

    def __str__(self):
        return f"{self.news.title} - Image"


class NewsVideo(models.Model):

    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="videos",
        verbose_name="Actualité"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Titre vidéo"
    )

    youtube_url = models.URLField(
        verbose_name="Lien YouTube"
    )

    class Meta:
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"

    def __str__(self):
        return self.title