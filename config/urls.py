from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ==================================================
    # ADMINISTRATION DJANGO
    # ==================================================
    path(
        "admin/",
        admin.site.urls
    ),

    # ==================================================
    # PAGES PRINCIPALES
    # ==================================================
    path(
        "",
        include("pages.urls")
    ),

    # ==================================================
    # ACTUALITÉS
    # ==================================================
    path(
        "actualites/",
        include("news.urls")
    ),

    # ==================================================
    # PRÉSIDENT DU MOUVEMENT
    # ==================================================
    path(
        "president/",
        include("leadership.urls")
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