from django.contrib import admin

from .models import (
    Category,
    News,
    NewsImage,
    NewsVideo
)


class NewsImageInline(admin.TabularInline):

    model = NewsImage

    extra = 1


class NewsVideoInline(admin.TabularInline):

    model = NewsVideo

    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_published",
        "published_at",
    )

    list_filter = (
        "category",
        "is_published",
        "published_at",
    )

    search_fields = (
        "title",
        "content",
        "excerpt",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "published_at",
    )

    inlines = [
        NewsImageInline,
        NewsVideoInline,
    ]

    fieldsets = (

        (
            "Informations générales",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "cover_image",
                    "excerpt",
                    "content",
                )
            }
        ),

        (
            "Publication",
            {
                "fields": (
                    "is_published",
                    "published_at",
                )
            }
        ),

        (
            "Documents",
            {
                "fields": (
                    "document",
                )
            }
        ),
    )


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):

    list_display = (
        "news",
        "caption",
    )

    search_fields = (
        "news__title",
        "caption",
    )


@admin.register(NewsVideo)
class NewsVideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "news",
    )

    search_fields = (
        "title",
        "news__title",
    )