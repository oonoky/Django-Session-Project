from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения movie.")

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")   

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>") 

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404<br>Страница не найдена</h1>')   

def pageForbidden(request, exception):
    return HttpResponseForbidden('<h1>Ошибка 403<br>Доступ запрещен</h1>')  

def pageBadrequest(request, exception) :
    return HttpResponseBadrequest('<h1>Ошибка 400<br>Невозможно обработать запрос</h1>')

def pageInternalServerError(request, exception):
    return HttpResponseInternalServerError('<h1>Ошибка 500<br>Ошибка сервера</h1>')
