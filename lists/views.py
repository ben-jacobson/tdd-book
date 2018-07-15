from django.shortcuts import redirect, render
#from django.core.exceptions import ValidationError
from lists.forms import ExistingListItemForm, ItemForm
from lists.models import List

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['text'])
    #    return redirect('/lists/the-only-list-in-the-world/')  # always re-direct a POST request, https://en.wikipedia.org/wiki/Post/Redirect/Get
    return render(request, 'home.html', {'form': ItemForm()})

'''def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})

    #return redirect(f'/lists/{list_.id}/')
    #return redirect('view_list', list_.id)
    return redirect(list_)'''

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        #Item.objects.create(text=request.POST['text'], list=list_)
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            #form.save(for_list=list_)
            form.save()
            #Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})