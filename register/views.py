from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import Profile

def register_usr(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('un')
        password1 = request.POST.get('pw')
        password2 = request.POST.get('pw')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('g1')
        phone_number = request.POST.get('pn')

        if password1 == password2:
            # Create a new User instance
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1,
            )

            # Create a new Profile instance
            profile = Profile.objects.create(
                user=user,
                date_of_birth=date_of_birth,
                gender=gender,
                phone_number=phone_number,
                avatar='profile_pictures/avatar.jpg'  # Assuming 'default_avatar.png' is the default profile picture
            )
            
            return redirect('login_user')  # Redirect to login page after successful registration
        else:
            # Passwords don't match, handle accordingly
            pass
    
    return render(request, 'registration.html')



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_usr(request):
    if request.method == "POST":
        email = request.POST.get('un')
        password = request.POST.get('pw')
        # Authenticate the user using Django's default authentication
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to the dashboard upon successful login
            return redirect('home')  # Adjust the URL pattern name for your dashboard
        else:
            # Handle incorrect credentials
            return render(request, 'Login.html', {'error_message': 'Invalid email or password'})
    else:
        # Render the login page for GET requests
        return render(request, 'Login.html')



def logout_usr(request):
    # Logout the user
    logout(request)
    # Redirect to the login page or any other page
    return redirect('home')