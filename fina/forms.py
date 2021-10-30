from django.forms import forms
from django.forms.models import ModelForm


from .models import *

# Form cuma untuk ganti profile picture
class ProfilePicForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # exclude => apa aja yang gak bisa diupdate
        exclude = ['user', 'member_since']


