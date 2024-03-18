from django.http import HttpResponse
from django.shortcuts import render 
from appointment.models import Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from inventory.models import Product
from room_mgmt.models import Room
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.conf import settings




def about(request):
    return render(request,"about.html")

def home(request):
    context = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile') and request.user.profile.avatar:
            context['avatar_url'] = request.user.profile.avatar.url
        else:
            # Use the default avatar URL if the user doesn't have an avatar
            context['avatar_url'] = settings.MEDIA_URL + 'profile_pictures/avatar.png'
    return render(request, 'home.html', context)

def facility(request):
    return render(request,"facility.html")

def login(request):
    return render(request,"templates/Login.html")

def registration(request):
    return render(request,"templates/registration.html")

def feed(request):
    return render(request,"templates/feed.html")

def vac(request):
    return render(request,"templates/vac.html")

def xray(request):
    return render(request,"templates/xray.html")

def physio(request):
    return render(request,"templates/physio.html")

def sono(request):
    return render(request,"templates/sono.html")

def patho(request):
    return render(request,"templates/patho.html")

def mri(request):
    return render(request,"templates/mri.html")

def ct(request):
    return render(request,"templates/ct.html")

def log(request):
    
    return render(request,"templates/Loginint.html")

def logg(request):
    return render(request,"templates/Login_inst.html")

def appoint(request):
    staff_users = User.objects.filter(is_staff=True)
    accepted_appointments = Appointment.objects.filter(accepted=True).values('time')
    accepted_time_slots = [appointment['time'].strftime('%I:%M %p') for appointment in accepted_appointments]
    available_time_slots = ["09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM", "03:00 PM"]
    print(available_time_slots)
    return render(request,"appointment.html",{'staff_users': staff_users,'accepted_time_slots': accepted_time_slots,'available_time_slots':available_time_slots})

def dash(request):
    return render(request,"templates/admindash.html")


def invent(request):
    products = Product.objects.all()
    return render(request,"templates/docdash.html",{'products': products})


@login_required
@staff_member_required(login_url='/stafflog/')
def doc(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(doctor=request.user)
        user_full_name = request.user.get_full_name()
        products = Product.objects.all()
        available_rooms = Room.objects.filter(available=True)
        unavailable_rooms = Room.objects.filter(available=False)
        # email_sent = request.session.get('email_sent', False)
        email_sent = request.session.pop('email_sent', False)
        reject_sent = request.session.pop('reject_sent', False)
        return render(request, 'docdash.html', {
            "data": appointments,
            'products': products,
            'available_rooms': available_rooms,
            'unavailable_rooms': unavailable_rooms,
            'user_full_name': user_full_name,
            'email_sent':email_sent,
            'reject_sent':reject_sent,
        })
    else:
        return redirect("login")  # Redirect to the login page if the user is not authenticated


def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = False
    room.save()
    return redirect('doc')

def release_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = True
    room.save()
    return redirect('doc')

def occupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = False
    room.save()
    return redirect('doc')  # Redirect to the doc page after occupying the room

def unoccupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = True
    room.save()
    return redirect('doc')

    # def docdash(request):
    # Assuming there's a logged-in doctor
    # if request.user.is_authenticated:
    #     doctor = request.user  # Assuming the doctor is stored in the request.user object
    #     appointments = Appointment.objects.all()
    #     appointments = Appointment.objects.filter(doctor=doctor)
    #     return render(request, 'docdash.html', {'appointments': appointments})
    # else:
    #     # Handle case where there's no logged-in doctor or doctor doesn't exist
    #     return render(request, 'error.html', {'message': 'You are not logged in as a doctor or do not have any appointments.'})
    


def staffreg(request):
    return render(request,'templates/staffreg.html')

