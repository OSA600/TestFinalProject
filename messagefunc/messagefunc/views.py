from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return HttpResponse("this is just a test")


def message(request):
    return render(request, "message.html")

