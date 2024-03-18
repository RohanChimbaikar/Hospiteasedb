# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('release/<int:room_id>/', views.release_room, name='release_room'),
    path('occupy/<int:room_id>/', views.occupy_room, name='occupy_room'),
    path('unoccupy/<int:room_id>/', views.unoccupy_room, name='unoccupy_room'),
]
