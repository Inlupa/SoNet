from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import News

# def article_search_display(request):
#     article_list = News.objects.all()
#     article_filter = ArticleFilter(request.GET, queryset=article_list)
#     return render(request, "insert_article/article_search_display.html", {'filter': article_filter})

def news_mainpage(request):
    news = News.objects.all()
    return render(request, "news/news_main.html", {'news':news })



# class NewsView(ListView):
#     model = News
#     template_name = 'news_card.html'
#     context_object_name = 'news'



