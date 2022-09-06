from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import News

# def article_search_display(request):
#     article_list = News.objects.all()
#     article_filter = ArticleFilter(request.GET, queryset=article_list)
#     return render(request, "insert_article/article_search_display.html", {'filter': article_filter})

def news_mainpage(request, object_id):
    instance = News.objects.all()
    news_url = instance.news_url
    news_anno = instance.news_anno
    news_name = instance.news_name

    return render(request, "news_card.html",
                  context={ 'object_id': object_id, 'news_url': news_url, 'news_name': news_name, 'news_anno':news_anno, 'instance':instance })


# class NewsView(ListView):
#     model = News
#     template_name = 'news_card.html'
#     context_object_name = 'news'



