import datetime
import random

from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user2.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.last_name = new_user.last_name.title()

            # new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'

            new_user.save()
            return redirect('login')

        #             # trimitere mail fara template
        #             new_subject = 'Confirmare cont in aplicatie'
        #             new_message = f''' Felicitari!
        #             Contul tau a fost adaugat cu success!
        #             Pentru autentificare username-ul este {new_user.username}
        #             '''
        #
        #             # send_mail(new_subject, new_message, EMAIL_HOST_USER, [new_user.email])
        #
        #             # trimitere mail CU TEMPLATE
        #             details_user = {
        #                 'fullname': f'{new_user.first_name} {new_user.last_name}',
        #                 'user_name': new_user.username
        #             }
        #             new_message = get_template('mail.html').render(details_user)
        #             mail = EmailMessage(
        #                 new_subject,
        #                 new_message,
        #                 EMAIL_HOST_USER,
        #                 [new_user.email]
        #             )
        #             mail.content_subtype = 'html'
        #             mail.send()
        #
        #             # Istoric
        #             msg = f'''A fost adaugat userul cu urmatoarele informatii: first_name={new_user.first_name},
        #             last_name = {new_user.last_name}, email={new_user.email}
        #             '''
        #             UserHistory.objects.create(
        #                 message=msg,
        #                 created_at=datetime.datetime.now(),
        #                 updated_at=datetime.datetime.now()
        #             )
        #

#
#
