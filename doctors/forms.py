from django import forms
from .models import Doctors
from .models import User


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

