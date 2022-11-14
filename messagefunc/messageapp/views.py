from django.http import HttpResponse
from django.shortcuts import render
from .models import Employees


def Employee(request):
    error = False
    if request.POST:
        data = request.POST
        if 'refAcces' in data and data.get('refAcces') != "":
            refAccesFin = data.get('refAcces')
        else:
            error = True
        if 'refOrdi' in data and data.get('refOrdi') != "":
            refOrdiFin = data.get('refOrdi')
        else:
            error = True
        if 'refPhone' in data and data.get('refPhone') != "":
            refPhoneFin = data.get('refPhone')
        else:
            error = True
        if not error:
            newEmp = Employees(refAcces=refAccesFin, refOrdi=refOrdiFin, refPhone=refPhoneFin)
            newEmp.save()
            return HttpResponse("saved !!!")
        else:
            return HttpResponse("there is an error ")
    else:
        return Employee(request)