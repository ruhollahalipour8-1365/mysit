from django.shortcuts import render

from django.http import HttpRequest, HttpResponse,JsonResponse

def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>home page</h1>')

def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>about page</h1>')

def contact_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>contact page</h1>')

