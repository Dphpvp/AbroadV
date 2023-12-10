from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationNewForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',  'username'
         ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your e-mail'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your new username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password'})