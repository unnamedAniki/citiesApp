from django.urls import path
from apps.users.form_views import LoginFormView, LogoutFormView


urlpatterns = [
    path('login/', LoginFormView.as_view(), name='user-login'),
    path('logout/', LogoutFormView.as_view(), name='user-logout'),
]