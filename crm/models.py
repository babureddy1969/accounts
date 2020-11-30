from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    qty = models.IntegerField(null=True,default=1)
    details = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2,default=0.00,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    def json(self):
        return {
            'id':self.pk,
            'name':self.name,
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
        return {'name':self.name,'phone':self.phone,'address':self.address}

class Order(models.Model):
    customer = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    cost = models.IntegerField(null=True, blank=True,default=0)
    paid = models.IntegerField(null=True, blank=True,default=0)
    balance = models.IntegerField(null=True, blank=True,default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def json(self):
        return {
            'customer':self.customer.json(),
            'cost':self.cost,
            'paid':self.paid,
            'balance':self.balance,
            'date':self.date_created,
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
            'date':self.date_created
        }
class Payment(models.Model):
    o = models.ForeignKey(Order,null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True, blank=True,default=0.00)
    create_date = models.DateTimeField(auto_now_add=True, null=True)


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
