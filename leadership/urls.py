from django.urls import path
from .views import leader_detail

urlpatterns = [

    path(
        "",
        leader_detail,
        name="leader"
    ),

]