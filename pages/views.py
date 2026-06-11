from django.shortcuts import render
from news.models import News


def home(request):

    latest_news = News.objects.filter(
        is_active=True
    ).order_by(
        "-published_at"
    )[:3]

    return render(
        request,
        "pages/home.html",
        {
            "latest_news": latest_news
        }
    )


def vision(request):

    return render(
        request,
        "pages/vision.html"
    )


def programme(request):

    return render(
        request,
        "pages/programme.html"
    )


def organisation(request):

    return render(
        request,
        "pages/organisation.html"
    )


def contact_page(request):

    return render(
        request,
        "pages/contact.html"
    )
def adhesion(request):
    return render(
        request,
        "pages/adhesion.html"
    )