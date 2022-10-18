from django import forms

from app_goods.models import ShoppingCart, Item, Good


class ItemForm(forms.Form):
    id = forms.CharField(required=False)
    name = forms.CharField(required=False)
    price = forms.CharField(required=False)


class ShoppingCartForm(forms.ModelForm):
    id = forms.HiddenInput()

    class Meta:
        model = ShoppingCart
        fields = ('id', 'count')


class ItemsForm(forms.ModelForm):
    id = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    company = forms.CharField(disabled=True)
    price = forms.CharField(disabled=True)

    class Meta:
        model = Item
        fields = ('id', 'company', 'price')


class GoodForm(forms.ModelForm):
    id = forms.HiddenInput()
    name = forms.CharField(disabled=True)
    description = forms.CharField(disabled=True)

    class Meta:
        model = Good
        fields = ('id', 'name', 'description')
