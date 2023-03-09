from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage
from .models import News
from django.views.generic import ListView


# def homepage(request):
#     news = News.objects.all().order_by('pub_date')
#     paginator = Paginator(news, 3)
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request,'mainpage/mainpage.html', context= {'page_obj': page_obj, 'news':news, })

class homepage(ListView):
    paginate_by = 3
    model = News
    template_name = "mainpage/mainpage.html"

def listing(request, page):
    keywords = News.objects.get_queryset().order_by("pub_date")
    paginator = Paginator(keywords, per_page=3)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "mainpage/mainpage.html", context)

def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 3)
    startswith = request.GET.get("startswith", "")
    keywords = News.objects.filter(
        news_name__startswith=startswith
    ).order_by("pub_date")
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"news_anno": contact.news_anno, "news_name": contact.news_name, "news_url": contact.news_url, "pub_date":contact.pub_date } for contact in page_obj.object_list]

    print(data)
    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }

    return JsonResponse(payload)



def about_provider(request):
    return render(request, 'mainpage/about_provider.html')
# def homepage(request):
#     # Все данные
#     news_list = News.objects.all()
#     # Функция пейджинга, 7 частей данных на страницу
#
#     paginator = Paginator(news_list, 1)
#
#     if request.method == 'GET':
#         # По умолчанию отображать данные первой страницы
#         news = paginator.page(1)
#         return render(request, 'mainpage/mainpage.html', context={'news': news })
#         # Взаимодействие с данными Ajax
#     if request.is_ajax():
#         page = request.GET.get('page')
#         try:
#             news = paginator.page(page)
#         # Если номер страницы не целое число, вернуться на первую страницу
#         except PageNotAnInteger:
#             news = paginator.page(1)
#         # Если номер страницы не существует / недопустим, вернуться на последнюю страницу
#         except InvalidPage:
#             news = paginator.page(paginator.num_pages)
#         news_li = list(news.object_list.values())
#         # Есть ли ложь / истина на предыдущей странице, есть ли ложь / истина на следующей странице, сколько страниц всего, данные текущей страницы
#         data = {'has_previous': news.has_previous(),
#                   'has_next': news.has_next(),
#                   'num_pages': news.paginator.num_pages,
#                   'news_li': news_li}
#         return JsonResponse(data)
