from django.shortcuts import render, HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('Hello world')

def a(request):
    return  HttpResponse('<div>Aa</div>' * 123123)