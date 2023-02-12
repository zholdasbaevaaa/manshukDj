from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import redirect, render


def index(request):
    # return render(request,'404page.html')
    return HttpResponse("FoodBlog")


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")


def archive(requset,year):
    if int(year) > 2020:
        return redirect('/')
    return HttpResponse(f"<h1>Archive</h1><p>{year}</p>")


def pageNotFound(request,exception):
    return HttpResponse('<h1>Страница не найдена</h1>')


# def acccesDenied(requset,exeption):
#     return HttpResponseNotFound('<h1>Доступ запрещен</h1>')
#
# def serverError(requset,exeption):
#     return HttpResponseNotFound('<h1>Невозможно обработать запрос</h1>')
#
# def forbidden(requset,exeption):
#     return HttpResponseNotFound('<h1>Невозможно обработать запрос</h1>')