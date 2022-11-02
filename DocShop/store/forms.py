from django import forms

from store.models import Order


class OrderForm(forms.ModelForm):
    quantity = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])

    class Meta:
        model = Order
        fields = ["quantity"]