from django.shortcuts import redirect, render
#from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from lists.models import List
from lists.forms import ExistingListItemForm, ItemForm, NewListForm

User = get_user_model()

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['text'])
    #    return redirect('/lists/the-only-list-in-the-world/')  # always re-direct a POST request, https://en.wikipedia.org/wiki/Post/Redirect/Get
    return render(request, 'home.html', {'form': ItemForm()})

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})
  
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})

def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    sharee_email = request.POST['sharee']

    # something the book doesn't tell you - if the user wasn't created prior, this view won't work.
    try:
        User.objects.get(email=sharee_email)
    except User.DoesNotExist:
        User.objects.create(email=sharee_email)

    list_.shared_with.add(sharee_email)
    return redirect(list_)