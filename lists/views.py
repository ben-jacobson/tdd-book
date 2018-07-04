from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')  # always re-direct a POST request, https://en.wikipedia.org/wiki/Post/Redirect/Get
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')