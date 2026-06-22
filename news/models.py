from django.db import models
from django.utils.text import slugify

from core.models import BaseModel


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nom"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="Slug"
    )

    class Meta:

        verbose_name = "Catégorie"

        verbose_name_plural = "Catégories"

        ordering = ["name"]

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name


class News(BaseModel):

    title = models.CharField(
        max_length=255,
        verbose_name="Titre"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="Catégorie"
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

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.title)

            slug = base_slug

            counter = 1

            while News.objects.filter(
                slug=slug
            ).exclude(
                pk=self.pk
            ).exists():

                slug = f"{base_slug}-{counter}"

                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

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