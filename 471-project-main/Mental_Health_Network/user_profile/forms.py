from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick_name', 'bio', 'profile_picture', 'address']
        labels = {
            'nick_name': 'Nickname',
            'bio': 'Biography',
            'profile_picture': 'Profile Picture',
            'address': 'Address',
        }
