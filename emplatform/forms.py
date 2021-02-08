from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Problem, Profile, Tip

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['company_name','status']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['names','image','description','phone','department']

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['pic', 'user','tip']       