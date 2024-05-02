import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import HospitalInvoice
from django.contrib import messages
from django.contrib.auth.models import Group
from django.urls import reverse

def create_invoice(request):
    success = False 
    if request.method == 'POST':
        # Create the invoice instance
        invoice = HospitalInvoice.objects.create(
            date=request.POST.get('date'),
            invoice_number=request.POST.get('invoiceNumber'),
            patient_name=request.POST.get('patientNameManual'),
            phone_number=request.POST.get('phone_number'),
            doctor=User.objects.get(id=request.POST.get('doctor')),
            total_amount_due=request.POST.get('totalAmountDue'),
            payment_status=request.POST.get('paymentStatus')
        )

        # Parse services list
        services = request.POST.getlist('services[]')
        amounts = request.POST.getlist('amounts[]')

        # Save services directly within the invoice object
        for service_name, service_amount in zip(services, amounts):
            if service_name and service_amount:
                # Create the service instance and add it to the invoice's services
                invoice.services.create(
                    name=service_name,  # You don't need these arguments here
                    amount=service_amount  # You don't need these arguments here
                )
        success = True 
        request.session['invoice_creation_success'] = success
        return render(request,'invoice_form.html',{'success':success}) 
    else:
        # Fetch all users to populate the doctor dropdown
        doctors = User.objects.filter(groups__name='doctors')
        return render(request, 'invoice_form.html', {'doctors': doctors})


def edit_invoice(request, invoice_id):
    # Retrieve the invoice object
    invoice = get_object_or_404(HospitalInvoice, id=invoice_id)

    if request.method == 'POST':
        # Retrieve data from the form
        date = request.POST.get('date')
        invoice_number = request.POST.get('invoiceNumber')
        patient_name = request.POST.get('patient_name')
        phone_number = request.POST.get('phone_number')
        doctor_id = request.POST.get('doctor')
        total_amount_due = request.POST.get('totalAmountDue')
        payment_status = request.POST.get('paymentStatus')

        # Update the invoice object with the new data
        invoice.date = date
        invoice.invoice_number = invoice_number
        invoice.patient_name = patient_name
        invoice.phone_number = phone_number
        invoice.doctor_id = doctor_id
        invoice.total_amount_due = total_amount_due
        invoice.payment_status = payment_status
        invoice.save()
        url = reverse('doc')

    # Append the fragment identifier
        url_with_fragment = f"{url}#bill-table"

    # Redirect to the URL with the fragment identifier
        return redirect(url_with_fragment)
    else:
        invoices = HospitalInvoice.objects.all()
        doctors_group = Group.objects.get(name='doctors')
        doctors = doctors_group.user_set.all()
        if not hasattr(invoice, 'date'):
            invoice.date = None
        print(invoices)
        # Render the edit invoice page with the invoice object
        return render(request, 'edit_invoice.html', {'invoice': invoice,'doctors': doctors})