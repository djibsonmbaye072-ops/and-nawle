from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Administration Django
    path(
        "admin/",
        admin.site.urls
    ),

    # Pages principales
    path(
        "",
        include("pages.urls")
    ),

    # Actualités
    path(
        "actualites/",
        include("news.urls")
    ),

]

# ==================================================
# MEDIA FILES (Images, PDF, Vidéos)
# ==================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )