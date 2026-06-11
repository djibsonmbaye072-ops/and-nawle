from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import News


def news_list(request):

    news = News.objects.filter(
        is_active=True
    ).order_by(
        "-published_at"
    )

    context = {
        "news_list": news
    }

    return render(
        request,
        "news/news_list.html",
        context
    )


def news_detail(request, pk):

    article = get_object_or_404(
        News,
        pk=pk,
        is_active=True
    )

    context = {
        "article": article
    }

    return render(
        request,
        "news/news_detail.html",
        context
    )