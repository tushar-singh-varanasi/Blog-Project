from django import forms
from .models import Politics,Contact,Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['Name','Email','Message']

class PoliticsForm(forms.ModelForm):
    class Meta:
        model=Politics
        fields=['title','slug','date','content','image','author']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        'date':forms.DateInput(attrs={'class':'date'}),
        'content':forms.Textarea(attrs={'class':'form-cantrol'}),
         } 

class BusnessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['title','slug','date','content','image','author']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        'date':forms.DateInput(attrs={'class':'date'}),
        'content':forms.Textarea(attrs={'class':'form-cantrol'}),
         } 

class Signup(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'myapp'}))
    password2=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'myapp'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        


class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}),
    )

