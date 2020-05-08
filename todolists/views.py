from django.shortcuts import redirect, render
from todolists.models import Item

# Create your views here.
def home_page(request):
    '''main page of the app'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
