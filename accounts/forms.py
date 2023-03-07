from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm 

 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['room_number'].required = True
        self.fields['profile_image'].required = False
    
class RegisterForm(forms.Form):
    name = forms.CharField(required=True)
    room_num = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput(), min_length=6)
    img = forms.ImageField(required=False)

class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)