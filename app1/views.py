from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app1(request):
    return HttpResponse('<h2>This is the first function</h2>')
def second_app1(request):
     return HttpResponse('<h2>This is the second function</h2>')
