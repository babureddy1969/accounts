from django.forms import ModelForm
from . models import Order, Supplier_slip, OrderDetails


class OrderDetailsForm(ModelForm):
    class Meta:
        model = OrderDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderDetailsForm,self).__init__(*args, **kwargs)
        # self.fields['customer'].empty_label = "-- select --"
        self.fields['product'].empty_label = "-- select --"
        self.fields['qty'].empty_label = "1"
        self.fields['cost'].empty_label = "0"
        self.fields['discount'].empty_label = "0"
        self.fields['final_cost'].empty_label = "0"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['customer'].empty_label = "-- select --"
        self.fields['product'].empty_label = "-- select --"

class Supplier_slipForm(ModelForm):
    class Meta:
        model = Supplier_slip
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Supplier_slipForm,self).__init__(*args, **kwargs)
        self.fields['supplier'].empty_label = "-- select --"
        self.fields['product'].empty_label = "-- select --"

