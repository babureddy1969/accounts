from django.shortcuts import render, redirect
from . models import  Customer, Order, Product, Product_stock,\
                        Customer_dena, Supplier, Supplier_slip, Supplier_pawna, Payment, OrderDetails
from . forms  import OrderForm, Supplier_slipForm, OrderDetailsForm
from . filters import OrderFilter, CustomerFilter
from django.db.models import Max, Min, Sum, Avg, Count, Value
from django.http.response import JsonResponse
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    sales = Order.objects.values('cost').annotate(a=Sum('cost')).values('a')[0]['a']
    expenses = Order.objects.values('cost').annotate(a=Sum('cost')).values('a')[0]['a']
    users = Customer.objects.all().count()
    visitors = Customer.objects.all().count()
    payments = Payment.objects.all().order_by('-create_date')

    context = {'orders': orders, 'customers': customers, 'sales': "{:,.0f}".format(sales) , 
        'expenses': "{:,.0f}".format(expenses) , 'users': users, 'visitors': visitors,'payments':payments}

    return render(request, 'crm/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'crm/products.html',{'products' : products})

def getProducts(request):
    products = Product.objects.all()
    data=[]
    for p in products:
        data+=[p.json()]
    return JsonResponse({'count':len(data),'data' : data})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customers.html',{'customers' : customers})

def customer_det(request,pk):
    return JsonResponse({'data':Customer.objects.get(pk=pk).json()})

def manager(request):
    return redirect('/admin/')

def savecustomer(request):
    id = request.GET.get("id",None)
    c = Customer()
    if id:
        c = Customer.objects.get(pk=id)
    c.name=request.GET.get('name','')
    c.phone=request.GET.get('tel1','')
    # c.tel2=request.GET.get('tel2','')
    c.address=request.GET.get('address','')
    c.save()
    customers = Customer.objects.all()
    return render(request, 'crm/customers.html',{'customers' : customers})

def customer_detail(request,pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = CustomerFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders':orders,'order_count':order_count, 'myFilter': myFilter}
    return render(request, 'crm/customer_detail.html', context) 

def customer_delete(request,pk):
    customer = Customer.objects.get(pk=pk).delete()
    return redirect('/customers/')

def orders(request):
    orders = Order.objects.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'orders' : orders, 'myFilter': myFilter}
    return render(request, 'crm/orders.html', context)

def orderdetailsdelete(request):
    OrderDetails.objects.filter(order=request.GET.get('orderid')).delete()
    return JsonResponse({'status':200})

def orderdetails(request,pk):
    orders = OrderDetails.objects.filter(order=pk)
    data=[]
    for o in orders:
        data+=[o.json()]
    # print(data)
    return JsonResponse({'count':len(data),'data':data})

def orderdetail(request):
    orderid = request.GET.get('orderid')
    itemno = request.GET.get('itemno')
    itemid = request.GET.get('itemid')
    if orderid==0:
        o=Order()
        orderid=o.save()
    od = OrderDetails()
    od.qty=request.GET.get('qty',1)
    od.order=Order(orderid)
    od.product=Product(itemid)
    od.cost=request.GET.get('cost')
    od.discount=request.GET.get('discount',0)
    od.final_cost=request.GET.get('final_cost')
    od.notes=request.GET.get('notes','')
    od.save()
    return JsonResponse({'status':200})

def createOrder(request):
    o=Order()
    o.customer=request.GET.get('customerid')
    o.cost=request.GET.get('cost',0)
    o.paid=request.GET.get('paid',0)
    o.balance=request.GET.get('balance',0)
    o.save()
    return JsonResponse({'status':200})

def updateOrder(request):
    order = Order.objects.get(id=pk)
    od=OrderDetails.objects.filter(order=pk).annotate(a=Sum('final_cost'))
    p=Payment.objects.filter(o=pk).annotate(a=Sum('amount'))
    if od: order.cost = od.a
    if p: order.paid = p.a
    order.balance=order.cost-order.paid
    order.save()
    return redirect('/orders/')

def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/orders/')

    context = {'item': order}
    return render(request,'crm/delete_order.html',context)


def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'crm/suppliers.html',{'suppliers' : suppliers})


def supplier_slip_list(request):
    supplier_slip_list = Supplier_slip.objects.all()

    # myFilter = OrderFilter(request.GET, queryset=orders)
    # orders = myFilter.qs

    context = {'supplier_slip_list' : supplier_slip_list}

    return render(request, 'crm/supplier_slip_list.html', context)


def createSupplier_slip(request):

    form = Supplier_slipForm()
    if request.method == 'POST':
        form = Supplier_slipForm(request.POST)
        if form.is_valid():
            form.save()
            product = form.cleaned_data['product']
            product_stock = Product_stock.objects.get(product=product)
            product_stock.quantity += form.cleaned_data['qty']
            print(product_stock.quantity)
            product_stock.save()
            return redirect('/supplier_slip_list/')

    context = {'form': form}
    return render(request,'crm/supplier_slip_form.html', context)

def updateSupplier_slip(request, pk):

    supplier_slip = Supplier_slip.objects.get(id=pk)
    form = Supplier_slipForm(instance=supplier_slip)

    if request.method == 'POST':
        form = Supplier_slipForm(request.POST, instance=supplier_slip)
        if form.is_valid():
            form.save()
            return redirect('/supplier_slip_list/')

    context = {'form': form}
    return render(request,'crm/supplier_slip_form.html', context)

def deleteSupplier_slip(request, pk):

    supplier_slip = Supplier_slip.objects.get(id=pk)
    if request.method == 'POST':
        supplier_slip.delete()
        return redirect('/supplier_slip_list/')

    context = {'item': supplier_slip}
    return render(request, 'crm/delete_supplier_slip.html',context)


def stocks(request):
    stock = Product_stock.objects.all()

    return render(request, 'crm/stock.html', {'stock' : stock})


def stock_detail(request):
    orders = Order.objects.all()
    supplier_slip_list = Supplier_slip.objects.all()

    context = {'orders': orders, 'supplier_slip_list': supplier_slip_list}

    return render(request, 'crm/stock_detail.html', context)


def dena_Pawna(request):
    customer_dena = Customer_dena.objects.all()

    return render(request, 'crm/dena_pawna.html', {'customer_dena':customer_dena})
