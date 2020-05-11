from django.shortcuts import redirect, render
from todolists.models import Item, List

# Create your views here.
def home_page(request):
    '''main page of the app'''
    return render(request, 'home.html')

def view_list(request):
    '''to-do list view'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    '''new to-do list view'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/unique-list/')
