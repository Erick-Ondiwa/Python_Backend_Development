from django.http import HttpResponse

def homepage(request):
  return HttpResponse("Hello, Welcome to my home page")

def aboutpage(request):
  return HttpResponse("This is the about page")