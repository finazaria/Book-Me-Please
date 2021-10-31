from django.forms import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import Profile

# Form cuma untuk ganti profile picture
class ProfilePicForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

class InterestForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['interest']




