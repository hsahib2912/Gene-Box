from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Enter your name in the URL in the format : localhost:port/sayhi/{{your name}}')

def hello(request,name):
    st = 'Hello '+name
    return HttpResponse(st)
