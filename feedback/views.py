# Import necessary modules
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

# Define your views here
def feedtxt(request):
    if request.method == "POST":
        try:
            # Get data from the POST request
            fn = request.POST.get("fname", "")
            ln = request.POST.get("lname", "")
            email = request.POST.get("em", "")
            satisfaction = request.POST.get("sat", "")
            feedback = request.POST.get("msg", "")

            # Connect to the database
            m = sql.connect(host="localhost", user="root", password="123456789", database="hospitease")
            cursor = m.cursor()

            # Insert data into the database using parameterized query
            c = "INSERT INTO feedback (fname, lname, email, status,additional_feedback) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(c, (fn, ln, email, satisfaction, feedback))
            m.commit()

        except sql.Error as e:
            # Handle database errors
            print("Database error:", e)

        finally:
            # Close the cursor and database connection
            if cursor:
                cursor.close()
            if m:
                m.close()

    return render(request, "feed.html")  # Assuming your feedback form template is named feedback.html
