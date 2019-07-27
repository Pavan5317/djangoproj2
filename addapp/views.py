from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'base.html')
def add(request):
    try:
        a=request.GET['t1']
        x=int(a)
        b=request.GET['t2']
        y=int(b)
        z=x+y
        return HttpResponse("""<html><body bgcolor=red><h1>Sum is:"""+str(z)+"""</h1></body></html>""")
    except(ValueError):
        return HttpResponse("invalid input")