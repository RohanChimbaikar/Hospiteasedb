# views.py
from django.shortcuts import render, redirect, get_object_or_404

from .models import Room

def room_list(request):
    available_rooms = Room.objects.filter(available=True)
    unavailable_rooms = Room.objects.filter(available=False)
    return render(request, 'room_list.html', {'available_rooms': available_rooms, 'unavailable_rooms': unavailable_rooms})

def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = False
    room.save()
    return redirect('room_list')

def release_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    room.available = True
    room.save()
    return redirect('room_list')


def occupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = False
    room.save()
    return redirect('room_list')

def unoccupy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.available = True
    room.save()
    return redirect('room_list')
