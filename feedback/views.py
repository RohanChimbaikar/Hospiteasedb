from django.shortcuts import render, redirect,HttpResponse
from .models import Feedback
from django.contrib import messages


from django.contrib.auth.decorators import login_required

@login_required
def feedback(request):
    if request.method == 'POST':
        # Extract form field values from request.POST
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        message = request.POST.get("message")
        
        # Validate form data (optional)
        if not (fname and lname and email and rating and message):
            # Handle invalid form data
            return HttpResponse("Invalid form data")

        # Save form data to the database
        feedback_instance = Feedback.objects.create(
            user=request.user,  # Save the current authenticated user
            first_name=fname,
            last_name=lname,
            email=email,
            stars=rating,
            message=message
        )
        feedback_instance.save()  # Render the feedback page with the success message
        return render(request, 'feedback.html', {'success_message': 'Thank you for your feedback! Your input helps us improve our service. We appreciate your time and insights'})

    else:
        return render(request, 'feedback.html')