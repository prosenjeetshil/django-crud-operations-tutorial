from django.shortcuts import redirect, render
from .forms import OrderForm
from .models import Orders

# Create your views here.
def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    obj = Orders.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)
