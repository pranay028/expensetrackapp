from django.urls import path
from . import views


urlpatterns = [
    path("user-register/", views.RegistrationView.as_view(), name="register_page"),
    path("user-login/", views.LoginView.as_view(), name="login_page")
]
