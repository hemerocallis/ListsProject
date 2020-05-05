from django.shortcuts import render

# Create your views here.
def home_page(request):
    '''main page of the app'''
    return render(request, 'home.html')
