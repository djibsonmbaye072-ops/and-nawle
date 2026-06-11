from django.urls import path

from .views import (
    home,
    vision,
    programme,
    organisation,
    contact_page,
    adhesion,
)

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "vision/",
        vision,
        name="vision"
    ),

    path(
        "programme/",
        programme,
        name="programme"
    ),

    path(
        "organisation/",
        organisation,
        name="organisation"
    ),

    path(
        "contact/",
        contact_page,
        name="contact"
    ),

    path(
        "adhesion/",
        adhesion,
        name="adhesion"
    ),

]