from django.shortcuts import render, get_object_or_404

from .models import News


def news_list(request):

    news_list = News.objects.filter(
        is_published=True
    )

    return render(
        request,
        "news/news_list.html",
        {
            "news_list": news_list
        }
    )


def news_detail(request, slug):

    article = get_object_or_404(
        News,
        slug=slug,
        is_published=True
    )

    return render(
        request,
        "news/news_detail.html",
        {
            "article": article
        }
    )