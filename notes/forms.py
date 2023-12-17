from django import forms
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data

        # get_email = cleaned_data['email']
        # check_emails = Notes.objects.filter(
        #     email=get_email)
        # if check_emails:
        #     msg = 'Exista un feedback de la acest user!'
        #     self._errors['email'] = self.error_class([msg])

        return cleaned_data
