from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/mainFood.html')




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