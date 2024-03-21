from django.shortcuts import render, redirect,get_object_or_404
from .models import BillingProfile, Invoice, Item, Payment
from .forms import InvoiceForm, PaymentForm

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})

def view_invoice(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    items = Item.objects.filter(invoice=invoice)
    return render(request, 'view_invoice.html', {'invoice': invoice, 'items': items})

def make_payment(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.invoice = invoice
            payment.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = PaymentForm()
    return render(request, 'make_payment.html', {'form': form, 'invoice': invoice})



from .forms import InvoiceForm
from .models import Invoice

def create_update_invoice(request, pk=None):
    if pk:
        invoice = get_object_or_404(Invoice, pk=pk)
    else:
        invoice = None

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', pk=invoice.pk)  # Redirect to the detail view of the created/updated invoice
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'invoice_form.html', {'form': form})


def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_detail.html', {'invoice': invoice})