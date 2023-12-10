from django import forms
from django.forms import TextInput, EmailInput

from notes.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'  # in formular se vor regasi toate fieldurile in ordinea definita in models.py

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'message': TextInput(attrs={'class': 'form-control', 'placeholder': 'Input message'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        # get_email = cleaned_data['email']
        # check_emails = Notes.objects.filter(
        #     email=get_email)
        # if check_emails:
        #     msg = 'Exista un feedback de la acest user!'
        #     self._errors['email'] = self.error_class([msg])

        return cleaned_data






