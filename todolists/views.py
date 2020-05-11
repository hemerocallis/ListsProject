from django.shortcuts import redirect, render
from todolists.models import Item, List

# Create your views here.
def home_page(request):
    '''main page of the app'''
    return render(request, 'home.html')

def view_list(request, list_id):
    '''to-do list view'''
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    '''new to-do list view'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    '''new item view to an existing list'''
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
