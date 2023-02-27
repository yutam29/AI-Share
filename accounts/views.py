from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.views import LogoutView

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

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

