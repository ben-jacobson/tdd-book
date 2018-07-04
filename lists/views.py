from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')  # always re-direct a POST request, https://en.wikipedia.org/wiki/Post/Redirect/Get

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})