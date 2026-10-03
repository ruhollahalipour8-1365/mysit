from django.shortcuts import render

from django.http import HttpRequest, HttpResponse,JsonResponse

def index_view(request: HttpRequest) -> HttpResponse:
    return render(request,'websit/index.html')

def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request,'websit/contact.html')

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request,'websit/about.html')

