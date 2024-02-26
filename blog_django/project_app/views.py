from django.shortcuts import render
from django.http import HttpResponse


def some_views(request):
    return HttpResponse('<h1>Hello!</h1>')
