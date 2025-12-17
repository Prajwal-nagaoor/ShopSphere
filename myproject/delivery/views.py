from django.shortcuts import render,redirect
from .forms import deliveryform
from django.contrib.auth.models import User
from .models import Deliverymodel
# Create your views here.
def delivery__from(request):
    user_details = User.objects.get(username = request.user)
    all 
    if request.method == 'POST':
        form = deliveryform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'order_placed.html')
    context = {
        'form': deliveryform(
            instance=user_details
        ),
        'data':Deliverymodel.objects.filter(username = request.user)
    }
    return render(request, 'delivery_form.html', context)
def update_order(request,pk):
    delivey_details = Deliverymodel.objects.get(id = pk)
    if request.method == 'POST':
        form = deliveryform(request.POST,delivey_details)
        if form.is_valid():
            form.save()
            return redirect('delivery_from')
    context = {
        'form': deliveryform(  
            instance=delivey_details
        )
    }
    return render(request,'update_order.html',context)