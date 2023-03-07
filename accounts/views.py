from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, RegisterForm, SigninForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login

@login_required
def profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    user = User.objects.get(username = request.user)
    try:
        Profile.objects.get(user = user)
        return redirect('index')
    except:
        if form.is_valid():
            form.save()
            return redirect('index')
    context= {'form' : form, 'user' : user}
    return render(request, 'accounts/profile.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            room_num = form.cleaned_data['room_num']
            password = form.cleaned_data['password']
            img = form.cleaned_data['img']
            user = User(
                username = room_num,
            )
            user.set_password(password)
            profile = Profile(
                user_name = name,
                room_number = room_num,
                profile_image = img,
                user = user,
            )
            user.save()
            profile.save()                
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')

        else:
            message = "エラー"
            context = {'form' : form, 'message' : message,}
            return render(request, 'accounts/register.html', context)
    else:
        form = RegisterForm()

    context= {'form' : form}
    return render(request, 'accounts/register.html', context)

class Signin(LoginView):
    form_class = SigninForm
    template_name = 'accounts/signin.html'

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

