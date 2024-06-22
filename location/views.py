from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("hello world")
def indiaMap(request):
    return render(request,'main/indiaMap.html',{})
def indiaLobby(request):
    return render(request, './indiaLobby.html', {})
def ok(request):
    return HttpResponse("ok")