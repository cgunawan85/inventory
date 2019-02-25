from django.forms import ModelForm

from .models import Product, InTransaction, OutTransaction


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_by', )


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
