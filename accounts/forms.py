from django import forms
from .models import Profile
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['room_number'].required = True
        self.fields['profile_image'].required = False
        