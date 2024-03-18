from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import HttpResponse
from django.http import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def book_appointment(request):
    if request.method == 'POST':
        doctor_email = request.POST.get('doctor')
        doctor_user = User.objects.get(email=doctor_email)
        date = request.POST.get('date')
        time = request.POST.get('selectedTime')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = Appointment.objects.create(doctor=doctor_user, date=date, time=time, name=name, email=email, phone=phone, message=message)
        appointments = Appointment.objects.all()  # Query all appointments again after creating the new one
        time_slots = {
        '09:00 AM': True,
        '09:30 AM': False,
        # Add more time slots as needed, with their disabled status
    }

        return render(request, 'appointment.html', {'appointment_details':True ,'time_slots':time_slots})
    
    else:
        return render(request, 'appointment.html')
    
    return render(request, 'appointment.html')




def send_acceptance_email(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        
        # Get the appointment object
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Send acceptance email
        send_mail(
            'Appointment Accepted',
            'Dear {},\n\n' \
                      'We are pleased to inform you that your appointment has been accepted.\n\n' \
                      'Appointment Details:\n' \
                      '- Date: {}\n' \
                      '- Time: {}\n' \
                      '- Doctor: {}\n\n' \
                      'We look forward to seeing you.\n\n' \
                      'Best regards,\n' \
                      'HospitEase Team'.format(appointment.name, appointment.date, appointment.time, appointment.doctor),
            'team@hospitease.com',
            [appointment.email],
            fail_silently=False,
        )
        request.session['email_sent'] = True
        appointment.accepted = True
        appointment.save()
        
        # Redirect to the URL of the other view
        return redirect('doc')
    else:
        request.session['email_sent'] = False
        return redirect('doc')
    

    




def reject_email(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        
        # Get the appointment object
        appointment = Appointment.objects.get(id=appointment_id)
        
        # Send acceptance email
        send_mail(
            'Appointment Rejection Notification',
            'Dear {},\n\n' \
            'We regret to inform you that your appointment scheduled for {} at {} with {} has been rejected.\n\n' \
            'Unfortunately, due to unforeseen circumstances, we are unable to accommodate your appointment request at this time. We apologize for any inconvenience this may cause.\n\n' \
            'Please feel free to reschedule your appointment at your earliest convenience by contacting our receptionist at:\n\n' \
            'Receptionist\'s Name: Emily Johnson\n' \
            'Receptionist\'s Email: emily.johnson@hospitease.com\n' \
            'Receptionist\'s Phone: +91 9372172051 \n\n' \
            'Thank you for your understanding.\n\n' \
            'Best regards,\n' \
            'HospitEase Team'.format(appointment.name, appointment.date, appointment.time, appointment.doctor),
            'team@hospitease.com',
            [appointment.email],
            fail_silently=False,
        )
        request.session['reject_sent'] = True
        
        # Redirect to the URL of the other view
        return redirect('doc')
    else:
        request.session['reject_sent'] = False
        return redirect('doc')
    

    