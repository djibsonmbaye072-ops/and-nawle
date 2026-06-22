from django.shortcuts import render
from .models import Leader


def leader_detail(request):

    leader = Leader.objects.first()

    return render(
        request,
        "leadership/leader_detail.html",
        {
            "leader": leader
        }
    )