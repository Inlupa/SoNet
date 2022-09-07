from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import News


def homepage(request):
    news = News.objects.order_by('pub_date')
    # news_url = instance.news_url
    # news_anno = instance.news_anno
    # news_name = instance.news_name
    return render(request,'mainpage/mainpage.html', {'news': news})

# def repair(request):
#     return render(request, "mainpage/repair.html")
#
# def looks(request):
#     return render(request, "mainpage/looks.html")
#
# def tech(request):
#     return render(request, "mainpage/tech.html")
