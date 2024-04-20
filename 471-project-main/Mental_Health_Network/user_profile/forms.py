from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['First_Name', 'Last_Name', 'mobile_number', 'bio', 'photo', 'address']
