from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
def index(request):
    nums = [1,2,3,4,5]
    hobby = ['볼링', '스쿼시', '산책']
    return render(request, 'index.html', {'my_list' : nums})

def coffee_view(request):
    # ...
    coffee_all = Coffee.objects.all()

    if request.method=="POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CoffeeForm()
    return render(request, 'coffee.html', {'coffee_list' : coffee_all, 'coffee_form': form})