from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("new-user-validation/", csrf_exempt(views.UserValidationView.as_view()),
         name="user_validation"),
    path("user-register/", views.RegistrationView.as_view(), name="register_page"),
    path("user-login/", views.LoginView.as_view(), name="login_page")
]
