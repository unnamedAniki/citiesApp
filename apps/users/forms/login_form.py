from django import forms
from django.shortcuts import redirect


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    @staticmethod
    def user_login(request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        from django.contrib.auth import authenticate
        from django.contrib.auth import login
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return redirect("/login")

    @staticmethod
    def user_logout(request):
        from django.contrib.auth import logout
        logout(request)
        return redirect("/")