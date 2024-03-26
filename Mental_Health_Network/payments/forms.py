from django import forms

class PaymentForm(forms.Form):
    bank_account_number = forms.CharField(max_length=20)
    mobile_number = forms.CharField(max_length= 11)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)