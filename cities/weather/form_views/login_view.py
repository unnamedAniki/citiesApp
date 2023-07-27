from django.urls import reverse
from django.views.generic import FormView
from ..forms import LoginForm


class LoginFormView(FormView):
    template_name = "forms/login_form.html"
    form_class = LoginForm
    success_url = "/"

    def form_invalid(self, form):
        return reverse("user-login")

    def post(self, request, *args, **kwargs):
        return LoginForm.user_login(self.request)

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutFormView(FormView):
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return LoginForm.user_logout(self.request)
