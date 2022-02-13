from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    """ registration form for users"""
    first_name = forms.CharField(max_length=50,label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Surname'}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')
        
    def __init__(self, *args , **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'