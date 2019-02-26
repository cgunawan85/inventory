from django.forms import ModelForm

from .models import Product, InTransaction, OutTransaction, Vendor


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_by', )


class AddVendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class InTransactionForm(ModelForm):
    class Meta:
        model = InTransaction
        fields = '__all__'
        exclude = ('created_by', )


class OutTransactionForm(ModelForm):
    class Meta:
        model = OutTransaction
        fields = '__all__'
        exclude = ('created_by', )
