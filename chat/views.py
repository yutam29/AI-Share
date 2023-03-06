from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.db.models import Q
from .models import Chat, ChatRoom
from .forms import ChatForm
from accounts.models import Profile
from app1.models import Item
import json
# Create your views here.


# チャット一覧表示
def chat(request):
    room = ChatRoom.objects.filter(Q(user1 = request.user.id) | Q(user2 = request.user.id)).order_by("-latest_date")
    try:
        user = Profile.objects.get(user = request.user)
        context = {'rooms': room, 'user': user}
    except:
        context = {'rooms' : room}
    return render(request, 'chat/chat.html', context)

# チャットルーム
def room(request, room_id):
    room = ChatRoom.objects.get(pk=room_id)
    chats = Chat.objects.filter(room = room_id)
    form = ChatForm()
    try:
        user = Profile.objects.get(user = request.user)
        context = {
        'room_name_json': mark_safe(json.dumps(room_id)),
        'room' : room,
        'user_name_json' : mark_safe(json.dumps(user.user_name)),
        'user_room_json' : mark_safe(json.dumps(user.room_number)),
        'user' : user,
        'form' : form,
        'chats' : chats,
        }
    except:
        context = {
        'room_name_json': mark_safe(json.dumps(room_id)),
        'room' : room,
        'form' : form,
        'chats' : chats,
        }
    return render(request, 'chat/room.html', context)

#チャットルーム作成
def making_room(request, item_id):
    user = Profile.objects.get(user = request.user)
    item = Item.objects.get(pk=item_id)
    room = ChatRoom.objects.filter((Q(user1 = user.id) & Q(user2 = item.user.id)) | (Q(user1 = user.id) & Q(user2 = item.user.id)))
    if room:
        return redirect('room', room_id = room[0].id)
    else:
        room = ChatRoom(
            user1 = user,
            user2 = item.user,
            )
        room.save()
        return redirect('room', room_id = room.id)
    
