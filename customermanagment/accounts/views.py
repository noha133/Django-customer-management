from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm , UserRegisterForm
from .filter import OrderFilter
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required







# Create your views here.
def registerpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else :
		form = UserRegisterForm()
		if request.method =='POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Account was created for ' +user)

				return redirect('loginpage')
		context = {'form': form}
		return render(request,'accounts/register.html',context)

def logoutUser(request):
	logout(request)
	return redirect('loginpage')

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		context = {}
		return render(request,'accounts/login.html',context)

@login_required(login_url='login')
def home (request):
    orders = order.objects.all()
    customers = Customer.objects.all()
    TotalOrders = orders.count()
    Pendingorders = orders.filter(status='Pending').count()
    Deliveredorders = orders.filter(status='Delivered').count()
    context = {'orders': orders , 'customers':customers , 'TotalOrders':TotalOrders , 'Pendingorders':Pendingorders , 'Deliveredorders':Deliveredorders}
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def products(request):
    products = product.objects.all()
    return render(request,'accounts/products.html', {'products': products})

@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()
	myFilter = OrderFilter(request.GET,queryset=orders)
	orders = myFilter.qs


	context = {'customer':customer, 'orders':orders, 'order_count':order_count,'myFilter': myFilter}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, order, fields=('product', 'status'), extra=5 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=order.objects.none(),instance=customer)
	if request.method == 'POST':
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request,pk):
    orders = order.objects.get(id=pk)
    form = OrderForm(instance=orders)
    context = {'form' :form}
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	orders = order.objects.get(id=pk)
	if request.method == "POST":
		orders.delete()
		return redirect('/')

	context = {'item':orders}
	return render(request, 'accounts/delete.html', context)