from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page (request):
    # TODO: Figure out how to render html to page
    return render(request,'index.html')

    # return HttpResponse("<h1> Hello world </h1>")

def test(request):
    # return HttpResponse("<p>Test Successful</p>")
    pass