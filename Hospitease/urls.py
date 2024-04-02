"""
URL configuration for Hospitease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Hospitease import views
from feedback.views import feedtxt
from appointment.views import *;
from Hospitease.views import dash
from adduser.views import register,logstaff,logout_view
from django.contrib.auth.views import LoginView
from inventory.views import add_product, delete_product,edit_product,use_product
from room_mgmt.views import occupy_room,unoccupy_room,release_room,book_room,room_list
from register.views import register_usr,login_usr,logout_usr
from billing.views import create_invoice,create_update_invoice,invoice_detail

# from appointment.views import bkapt

admin.site.site_header="HospitEase"
admin.site.site_title="HospitEase Dashboard"

urlpatterns = [
    # Home Page
    path('profile.html',views.profile,name='pfpage'),
    path('admin/', admin.site.urls),
    path('', views.home),
    path('templates/home.html', views.home,name='home'),
    path('templates/facility.html',views.facility),
    path('templates/about.html/', views.about),
    path('templates/Login.html', views.login,name="login_user"),
    path('templates/registration.html',views.registration),
    path('templates/feed.html',views.feed),
    path('loginint/', views.doc, name='loginst'),
    path("templates/Loginint.html",views.log,name='red'),
    path('templates/Login_inst.html',views.logg),
   path('templates/appointment.html', views.appoint),
   path('appointment/',book_appointment,name='bookappointment'),
   path('register_usr',register_usr,name="register_usr"),
   path('login_usr',login_usr,name='login_usr'),
   path('logout_usr/', logout_usr, name='logout_usr'),

   
    # Facility
    path('templates/vac.html',views.vac),
    path('templates/xray.html',views.xray),
    path('templates/physio.html',views.physio),
    path('templates/sono.html',views.sono),
    path('templates/patho.html',views.patho),
    path('templates/xray.html',views.xray),
    path('templates/mri.html',views.mri),
    path('templates/ct.html',views.ct),

    path('templates/admindash.html',views.dash),
    path('templates/docdash.html',views.doc,name='doc'),
    path('send-acceptance-email/', send_acceptance_email, name='send_acceptance_email'),
    path('reject-appointment/', reject_email, name='reject_appointment'),
    path('get_time_slots/', views.get_time_slots, name='get_time_slots'),

    
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('release/<int:room_id>/', views.release_room, name='release_room'),
    
     path('occupy/<int:room_id>/', views.occupy_room, name='occupy_room'),
    path('unoccupy/<int:room_id>/', views.unoccupy_room, name='unoccupy_room'),
   
    path('templates/staffreg.html', views.staffreg),
    path('registaff',register,name='registaff'),
    path('stafflog',logstaff,name='stafflog'),
    path('logout/', logout_view, name='logout'),



     path('accounts/login/', LoginView.as_view(), name='login'),



     path('templates/inventory.html',views.invent,name='invent'),
     #Inventory
     path('add_product/', add_product, name='add_product'),
     path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('delete_product/<int:pk>/',delete_product, name='delete_product'),
    path('use_product/<int:product_id>/', use_product, name='use_product'),
    
    #Rooms management
    path('rooms/', views.doc, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('release/<int:room_id>/', views.release_room, name='release_room'),
    path('occupy/<int:room_id>/', views.occupy_room, name='occupy_room'),
    path('unoccupy/<int:room_id>/', views.unoccupy_room, name='unoccupy_room'),



    #Billing
    path('invoice/create/', create_update_invoice, name='create_invoice'),
    path('invoice/update/<int:pk>/', create_update_invoice, name='update_invoice'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice_detail'),
    path('edit_profile',views.edit_profile,name='edit_profile'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
