from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1> welcome to home page </h1>")    