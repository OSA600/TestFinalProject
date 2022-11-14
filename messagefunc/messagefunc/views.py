from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD


=======
>>>>>>> a06150f575cdd359d5ce47b4b2ec32cbf157ffa2


def index(request):
    return HttpResponse("this is just a test")


def message(request):
    return render(request, "message.html")

