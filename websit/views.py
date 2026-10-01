from django.shortcuts import render

from django.http import HttpRequest, HttpResponse,JsonResponse

def http_test(request: HttpRequest) -> HttpResponse:
    return HttpResponse("سلام دنیا!")

def json_test(request: HttpRequest) -> HttpResponse:
    return JsonResponse({'neme':'ali'})
# Create your views here.
