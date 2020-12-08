from django.shortcuts import render, redirect
from . models import  Customer, Order, Product, Product_stock,\
                        Customer_dena, Supplier, Supplier_slip, Supplier_pawna, Payment, OrderDetails
from . forms  import OrderForm, Supplier_slipForm, OrderDetailsForm
from . filters import OrderFilter, CustomerFilter
from django.db.models import Max, Min, Sum, Avg, Count, Value
from django.http.response import JsonResponse
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    orders = Order.objects.all().order_by('-cost')
    customers = Customer.objects.all()
    sales = Order.objects.all().aggregate(Sum('cost'))['cost__sum']
    balance = Order.objects.all().aggregate(Sum('balance'))['balance__sum']
    users = Customer.objects.all().count()
    visitors = Customer.objects.all().count()
    payments = Order.objects.filter(balance__gt=0).order_by('-balance')

    context = {'orders': orders, 'customers': customers, 'sales': "{:,.0f}".format(sales) , 
        'balance': "{:,.0f}".format(balance) , 'users': users, 'visitors': visitors,'payments':payments}
    print(context)
    return render(request, 'crm/dashboard.html',context)
def todaysGoldPrice(request):
    return JsonResponse({'data':todaysGoldRate()})#
def todaysGoldRate():
    url="https://www.policybazaar.com/gold-rate-bangalore/"
    import urllib3
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    http = urllib3.PoolManager()
    r = http.request('GET', url,headers=hdr)
    html = r.data.decode("utf-8") 
    i=html.find("<td>Today</td>")+15
    i=html.find("<td>",i)+4
    i1=html.find("</td>",i)
    return html[i:i1]

def products(request):
    products = Product.objects.all()
    return render(request, 'crm/products.html',{'products' : products})

def getProducts(request,c):
    products = Product.objects.filter(category=c)
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
    orders = Order.objects.filter(category=request.GET.get('category'))
    category_name = 'Saree' if request.GET.get('category')=='S' else 'Jewellery' 
    context = {'customer': customer, 'orders':orders,'order_count':len(orders),'category':category_name,'category_type':request.GET.get('category'),"gold_rate":todaysGoldRate()}
    return render(request, 'crm/customer_detail.html', context) 

def customer_delete(request,pk):
    customer = Customer.objects.get(pk=pk).delete()
    return redirect('/customers/')

def orders(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'orders' : orders, 'myFilter': myFilter,'customers':customers}
    return render(request, 'crm/orders.html', context)

def orderdetailsdelete(request):
    OrderDetails.objects.filter(order=request.GET.get('orderid')).delete()
    return JsonResponse({'status':200})

def orderdetails(request,pk):
    orders = OrderDetails.objects.filter(order=pk).order_by('itemno')
    data=[]
    for o in orders:
        data+=[o.json()]
    print(data)
    return JsonResponse({'count':len(data),'data':data})

def orderdetail(request):
    customerid = request.GET.get('customerid')
    orderid = request.GET.get('orderid')
    itemno = request.GET.get('itemno')
    itemid = request.GET.get('itemid')
    od = OrderDetails()
    od.itemno=itemno
    od.qty=request.GET.get('qty',1)
    od.order=Order(orderid)
    od.product=Product(itemid)
    od.cost=request.GET.get('cost')
    od.discount=request.GET.get('discount',0)
    od.final_cost=request.GET.get('final_cost')
    od.notes=request.GET.get('notes','')
    # print(od.json())
    od.save()    
    return JsonResponse({'status':200})

def createOrder(request):
    o=Order()
    o.customer=Customer(request.GET.get('customerid'))
    o.gold_price=request.GET.get('gold_price',0)
    o.category=request.GET.get('category','S')
    o.cost=request.GET.get('cost',0)
    o.paid=request.GET.get('paid',0)
    o.balance=request.GET.get('balance',0)
    o.qty=request.GET.get('qty',1)
    o.save()
    oid = Order.objects.latest('id').pk
    # print(oid)
    return JsonResponse({'status':200,"orderid":oid})

def customer_payments(request,customerid):
    p=Payment.objects.filter(order__customer__id=customerid)
    #print(p)
    data=[]
    for d in p:        
        data+=[d.json()]
    return JsonResponse({'count':len(data),'data':data})

def payments(request):
    p=Payment.objects.filter(order__id=request.GET.get('orderid'))
    #print(p)
    data=[]
    for d in p:        
        data+=[d.json()]
    return JsonResponse({'count':len(data),'data':data})

def createPayment(request):
    o=Order.objects.get(pk=request.GET.get('orderid'))
    p=Payment()
    p.order=o
    p.amount=request.GET.get('amount')
    p.payment_method=request.GET.get('payment_method')
    p.notes=request.GET.get('notes')
    p.save()
    o.paid+=int(p.amount)    
    o.balance-=int(p.amount)    
    o.save()
    return JsonResponse(p.json())
# def updateOrder(request):
#     order = Order.objects.get(id=pk)
#     od=OrderDetails.objects.filter(order=pk).annotate(a=Sum('final_cost'))
#     q=OrderDetails.objects.filter(order=pk).annotate(a=Sum('qty'))
#     p=Payment.objects.filter(o=pk).annotate(a=Sum('amount'))
#     if od: order.cost = od.a
#     if p: order.paid = p.a
#     if q: order.qty = q.a
#     order.balance=order.cost-order.paid
#     order.save()
#     return redirect('/orders/')
# def update_order(pk):
#     order = Order.objects.get(id=pk)
#     od=OrderDetails.objects.filter(order=pk).annotate(a=Sum('final_cost'))
#     q=OrderDetails.objects.filter(order=pk).annotate(a=Sum('qty'))
#     p=Payment.objects.filter(o=pk).annotate(a=Sum('amount'))
#     if od: order.cost = od.a
#     if p: order.paid = p.a
#     if q: order.qty = q.a
#     order.balance=order.cost-order.paid
#     order.save()
#     return {'status':200}

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
