from django.db import models
from datetime import datetime, date, timedelta
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=1,default='S',null=True)
    wt = models.DecimalField(max_digits=10,decimal_places=2,null=True,default=0.00)
    making_charges = models.DecimalField(max_digits=10,decimal_places=2,null=True,default=22.00)
    qty = models.IntegerField(null=True,default=1)
    details = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0.00,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    def json(self):
        return {
            'id':self.pk,
            'name':self.name,
            'category':self.category,
            'wt':self.wt,
            'making_charges':self.making_charges,
            'qty':self.qty,
            'details':self.details,
            'price':self.price,
            'date':self.date_created
        }

class Product_stock(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    previous_quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def json(self):
        return {'name':self.name,'phone':self.phone,'address':self.address,'date':datetime.strftime(self.create_date,'%d-%m-%Y %H:%M'),}

class Order(models.Model):
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    category = models.CharField(max_length=1,default='S',null=True)
    cost = models.IntegerField(null=True, blank=True,default=0)
    paid = models.IntegerField(null=True, blank=True,default=0)
    balance = models.IntegerField(null=True, blank=True,default=0)
    qty = models.IntegerField(null=True, blank=True,default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def json(self):
        return {
            'customer':self.customer.json(),
            'category':self.category,
            'cost':self.cost,
            'paid':self.paid,
            'balance':self.balance,
            'qty':self.qty,
            'date':datetime.strftime(self.date_created,'%d-%m-%Y %H:%M'),
        }
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, null= True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL)
    itemno = models.IntegerField(null=True,default=1)
    qty = models.IntegerField(null=True,default=1)
    cost = models.IntegerField(null=True,default=0)
    final_cost = models.IntegerField(null=True, blank=True,default=0)
    discount = models.IntegerField(null=True, blank=True,default=0)
    notes=models.CharField(null=True,blank=True,default='',max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def json(self):
        return {
            'order':self.order.id,
            'product':self.product.id,
            'itemno':self.itemno,
            'qty':self.qty,
            'cost':self.cost,
            'final_cost':self.final_cost,
            'discount':self.discount,
            'notes':self.notes,
            'date':datetime.strftime(self.date_created,'%d-%m-%Y %H:%M'),
            "new":0
        }
class Payment(models.Model):
    order = models.ForeignKey(Order,null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True, blank=True,default=0.00)
    payment_method = models.CharField(null=True, blank=True,default='Cash',max_length=20)
    notes = models.CharField(null=True, blank=True,default='Cash',max_length=50)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    def json(self):
        return{
            'order':self.order.pk,
            'amount':self.amount,
            'payment_method':self.payment_method,
            'notes':self.notes,
            'date':datetime.strftime(self.create_date,'%d-%m-%Y %H:%M'),
            "new":0,
        }

class Customer_dena(models.Model):
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    final_cost = models.IntegerField(null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Supplier_slip(models.Model):
    supplier = models.ForeignKey(Supplier, null= True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL)
    delivery_place = models.CharField(max_length=200, null=True)
    qty = models.IntegerField(null=True,default=0)
    cost = models.IntegerField(null=True)
    final_cost = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Supplier_pawna(models.Model):
    supplier = models.ForeignKey(Supplier, null= True, on_delete= models.SET_NULL)
    Amount = models.IntegerField(null=True)
