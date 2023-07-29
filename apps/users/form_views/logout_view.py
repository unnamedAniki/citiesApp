from django.views.generic import FormView
from apps.users.forms import LoginForm


class LogoutFormView(FormView):
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return LoginForm.user_logout(self.request)