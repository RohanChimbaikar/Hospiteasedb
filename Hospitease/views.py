from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from appointment.models import Appointment, Doctor
from inventory.models import Product
from room_mgmt.models import Room
from Department.models import Department



def about(request):
    # Retrieve the head of departments
    head_of_departments = User.objects.filter(departments__head_of_department__isnull=False)
    
    # Retrieve all doctors
    doctors = User.objects.filter(groups__name='Doctors')
    
    return render(request, "about.html", {'head_of_departments': head_of_departments, 'doctors': doctors})

def profile(request):
    return render(request,'templates/profile.html')

def home(request):
    context = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile') and request.user.profile.avatar:
            context['avatar_url'] = request.user.profile.avatar.url
        else:
            # Use the default avatar URL if the user doesn't have an avatar
            context['avatar_url'] = settings.MEDIA_URL + 'profile_pictures/avatar.png'
        
        # Check if the user belongs to the 'Doctors' group
        is_doctor = request.user.groups.filter(name='Doctors').exists()
        context['is_doctor'] = is_doctor

    return render(request, 'home.html', context)

def facility(request):
    context = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile') and request.user.profile.avatar:
            context['avatar_url'] = request.user.profile.avatar.url
        else:
            # Use the default avatar URL if the user doesn't have an avatar
            context['avatar_url'] = settings.MEDIA_URL + 'profile_pictures/avatar.png'
        
        # Check if the user belongs to the 'Doctors' group
        is_doctor = request.user.groups.filter(name='Doctors').exists()
        context['is_doctor'] = is_doctor

    return render(request,"facility.html",context)

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


def get_time_slots(request):
    if request.method == 'GET':
        doctor_username = request.GET.get('doctor')
        if doctor_username:
            try:
                doctor = Doctor.objects.get(user__username=doctor_username)
                time_slots = [str(slot) for slot in doctor.time_slots.all()]
                if not time_slots:
                    return JsonResponse({'message': 'No time slots available for this doctor'}, status=200)
                else:
                    return JsonResponse(time_slots, safe=False)
            except Doctor.DoesNotExist:
                return JsonResponse({'error': 'Doctor not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def custom_login_required(login_url=None):
    def decorator(view_func):
        actual_decorator = user_passes_test(
            lambda u: u.is_authenticated,
            login_url=login_url,
        )
        return actual_decorator(view_func)
    return decorator



@custom_login_required(login_url='/templates/Login.html')
def appoint(request):
    context = {}
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile') and request.user.profile.avatar:
            context['avatar_url'] = request.user.profile.avatar.url
        else:
            # Use the default avatar URL if the user doesn't have an avatar
            context['avatar_url'] = settings.MEDIA_URL + 'profile_pictures/avatar.png'
    
    # Retrieve staff users and accepted appointments
    staff_users = User.objects.filter(is_staff=True).exclude(username='admin').prefetch_related('departments').all()
  
    
    # Retrieve doctors from the "Doctors" group
    doctor_group = Group.objects.get(name='Doctors')
    doctors = doctor_group.user_set.all()
    
    # Initialize a list to store available time slots
    available_time_slots = []
    accepted_time_slots = []
    
    # Loop through each doctor and retrieve their time slots
    for doctor in doctors:
        try:
            # Retrieve the associated Doctor object for the user
            doctor_profile = doctor.doctor_profile  # Assuming a OneToOneField to Doctor model
            
            # Access the time slots associated with the doctor profile
            time_slots = doctor_profile.time_slots.all()
            
            # Append the time slots to the list
            available_time_slots.extend(time_slots)
        except ObjectDoesNotExist:
            # Handle the case where the doctor profile does not exist for the user
            pass
    
    return render(request, "appointment.html", {'staff_users': staff_users, 'accepted_time_slots': accepted_time_slots, 'available_time_slots': available_time_slots, 'avatar_url': context.get('avatar_url', None)})


def dash(request):
    return render(request,"templates/admindash.html")


def invent(request):
    products = Product.objects.all()
    return render(request,"templates/docdash.html",{'products': products})

from django.shortcuts import render, redirect
from django.conf import settings

from django.contrib.auth.models import User, Group

@login_required
@staff_member_required(login_url='/stafflog/')
def doc(request):
    # Retrieve head of departments
    head_of_departments = User.objects.filter(departments__head_of_department__isnull=False)
    
    # Retrieve all doctors along with their departments
    doctors = User.objects.filter(groups__name='Doctors')
    
    # Add fetched data to the context
    context = {
        'head_of_departments': head_of_departments, 
        'doctors': doctors
    }

    if request.user.is_authenticated:
        # Check if the user has a profile picture
        if hasattr(request.user, 'profile') and request.user.profile.avatar:
            context['avatar_url'] = request.user.profile.avatar.url
        else:
            # Use the default avatar URL if the user doesn't have an avatar
            context['avatar_url'] = settings.MEDIA_URL + 'profile_pictures/avatar.png'
        
        # Fetch other data if user is authenticated
        appointments = Appointment.objects.filter(doctor=request.user)
        user_full_name = request.user.get_full_name()
        products = Product.objects.all()
        available_rooms = Room.objects.filter(available=True)
        unavailable_rooms = Room.objects.filter(available=False)
        email_sent = request.session.pop('email_sent', False)
        reject_sent = request.session.pop('reject_sent', False)
        department_info = Department.objects.filter(doctors=request.user).first()
        dob=request.user.profile.date_of_birth
        print(dob)
        print(department_info)
        print(request.user.profile.gender)
        # Add fetched data to the context
        context.update({
            "data": appointments,
            'products': products,
            'available_rooms': available_rooms,
            'unavailable_rooms': unavailable_rooms,
            'user_full_name': user_full_name,
            'email_sent': email_sent,
            'reject_sent': reject_sent,
            'department':department_info,
        })
        
        # Render the template with the combined context
        return render(request, 'docdash.html', context)
    else:
        return redirect("login")
  # Redirect to the login page if the user is not authenticated
  # Redirect to the login page if the user is not authenticated


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

def edit_profile(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        phone=request.POST.get('phoneNumber')
        gender=request.POST.get('gender')
        address = request.POST.get('address')
        medical_school = request.POST.get('medicalSchool')
        date_of_birth = request.POST.get('dateOfBirth')
        license_number = request.POST.get('licenseNumber')
        
        # Update the profile data
        profile = request.user.profile
        profile.gender = gender
        profile.email=email
        profile.phone_number=phone
        profile.address = address
        profile.medical_school = medical_school
        profile.date_of_birth = date_of_birth
        profile.license_number = license_number
        profile.save()
                
        # Redirect to some page after saving changes
        return redirect('doc')  # Redirect to profile page or any other page
    else:
        # Handle GET request, if needed
        
        return render(request, 'docdash.html', {'success_message': messages.get_messages(request)})