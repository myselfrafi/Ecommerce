from django import forms

from .models import Register

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    c_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Register
        fields = ['name','phone_no','email','password','c_password','gender']


    def clean(self):
        cleaned_data = super().clean()

        pwd = cleaned_data['password']
        c_pwd = cleaned_data['c_password']

        if(pwd!=c_pwd):
            raise forms.ValidationError("Passwords does not Matched..X X X")

        return cleaned_data

    
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())