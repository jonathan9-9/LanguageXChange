from django import forms
from accounts.models import User


# class RegistrationForm(forms.Form):
#     first_name = forms.CharField(max_length=150)
#     last_name = forms.CharField(max_length=150)
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     city = forms.CharField(max_length=150)
#     state = forms.CharField(max_length=150)
#     country = forms.CharField(max_length=150)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'city', 'state', 'country')
