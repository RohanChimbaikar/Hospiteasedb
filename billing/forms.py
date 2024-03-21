from django import forms
from .models import Invoice, Payment


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['patient', 'total_amount', 'status', 'due_date', 'notes']

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget.attrs.update({'class': 'datepicker'})  # Add a CSS class for datepicker


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['invoice', 'amount_paid', 'payment_method', 'payment_status', 'notes']
