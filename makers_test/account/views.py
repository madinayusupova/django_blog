from django.contrib.auth.models import User
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'