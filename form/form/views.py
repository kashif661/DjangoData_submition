from django.http import HttpResponse
from django.shortcuts import render
from submit.models import Submit

def index(request):
    de = Submit.objects.all()
    #print(de)
    return render(request, "index.html" , {'de' : de})