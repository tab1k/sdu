from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from users.forms import UserLoginForm


class SignInView(LoginView):
    template_name = 'users/sign_in.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('portal:home')