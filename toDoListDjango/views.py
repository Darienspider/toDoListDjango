from django.shortcuts import render
# Create your views here.
def home_page(request):
    render(template_name="index.html")