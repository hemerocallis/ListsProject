from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    '''main page of the app'''
    return HttpResponse('<html><title>To-Do lists</title></html>')
