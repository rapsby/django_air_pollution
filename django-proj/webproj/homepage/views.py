from django.shortcuts import HttpResponse, render
from plotly.offline import plot
from plotly.graph_objs import Scatter, Heatmap
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

def air_pollution_view(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "air_pollution.html", context={'plot_div': plot_div})
