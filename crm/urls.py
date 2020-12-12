from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="dashboard"),
    path('products/', views.products, name="products"),
    path('getProducts/<str:c>/', views.getProducts, name="getProducts"),
    path('manager/', views.manager, name="manager"),

    #stock
    path('product_stocks/', views.stocks, name="stocks"),
    path('stock_detail/', views.stock_detail, name="stock_detail"),

    #customer
    path('customers/', views.customers, name="customers"),
    path('customer_det/<str:pk>/',views.customer_det, name="customer_det"),
    path('customer/<str:pk>/',views.customer_detail, name="customer_detail"),
    path('savecustomer/',views.savecustomer, name="savecustomer"),
    path('customer_delete/<str:pk>/',views.customer_delete, name="customer_delete"),

    #supplier
    path('suppliers/',views.suppliers, name="suppliers"),
    path('supplier/<str:pk>/',views.customer_detail, name="supplier_detail"),

    #supplier slip
    path('supplier_slip_list/', views.supplier_slip_list, name="supplier_slip_list" ),
    path('supplier_slip/',views.createSupplier_slip, name="create_supplier_slip" ),
    path('update_supplier_slip_list/<str:pk>/',views.updateSupplier_slip, name="update_supplier_slip" ),
    path('delete_supplier_slip_list/<str:pk>/',views.deleteSupplier_slip, name="delete_supplier_slip" ),

    #order
    path('orders/', views.orders, name="orders" ),
    # path('showorders/', views.ShowOrders, name="ShowOrders" ),
    path('order/<str:pk>', views.orderdetails, name="orderdetails" ),
    path('order_slip/',views.createOrder, name="create_order" ),
    # path('update_order/<str:pk>/',views.updateOrder, name="update_order" ),
    path('delete_order/<str:pk>/',views.deleteOrder, name="delete_order" ),
    path('updateOrder/<str:pk>/',views.updateOrder, name="updateOrder" ),

    #order detail
    path('orderdetail/',views.orderdetail, name="orderdetail" ),
    path('orderdetailsdelete/',views.orderdetailsdelete, name="orderdetailsdelete" ),
    path('orderdetaildelete/<str:pk>/',views.orderdetaildelete, name="orderdetaildelete" ),
    path('createOrder/',views.createOrder, name="createOrder"),
    #payment
    path('payments/', views.payments, name="payments" ),
    path('customer_payments/<str:customerid>', views.customer_payments, name="customer_payments" ),
    path('createPayment/',views.createPayment, name="createPayment"),
    #dena pawna
    path('dena_pawna/', views.dena_Pawna, name="denapawna"),


    path('todaysGoldPrice/', views.todaysGoldPrice, name="todaysGoldPrice"),

]
