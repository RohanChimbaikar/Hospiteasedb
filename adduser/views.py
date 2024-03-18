from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        username = email  # Set username to email
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')

        # Check if passwords match
        if password != password2:
            # Handle password mismatch error
            return HttpResponse("Passwords do not match")

        # Check if user with the same email already exists
        if User.objects.filter(email=email).exists():
            # Handle user already exists error
            return HttpResponse("User with this email already exists")

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.save()

        # Redirect to login page after successful registration
        return redirect('stafflog')

    # Render registration form for GET requests
    return render(request, 'staffreg.html')


def logstaff(request):
    if request.method == "POST":
        uname = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(request, username=uname, password=pw)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard upon successful login
            return redirect('templates/docdash.html')  # Assuming 'docdash' is the name of the URL pattern for the dashboard
        else:
            # Handle incorrect credentials
            return render(request, 'Loginint.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login page for GET requests
        return render(request, 'Loginint.html')
    
def logout_view(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect('stafflog')  





