# from django.http import HttpResponse

from django.shortcuts import render

def homepage(request):
  # return HttpResponse("Hello, Welcome to my home page")

  return render(request, 'home.html')

def aboutpage(request):
  # return HttpResponse("This is the about page")

  return render(request, 'about.html')