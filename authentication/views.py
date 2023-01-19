from django.shortcuts import render
from django.views import View
# Create your views here.
import json
from django.contrib.auth.models import User
from django.http import JsonResponse


class UserValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        username = data["usernameField"]
        user_email = data["emailField"]
        user_password = data["passwordField"]

        if not username.isalnum():
            return JsonResponse({"message": "username should be alphanumeric"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "username already taken"}, status=403)
        # print(username, user_email, user_password)
        return JsonResponse({"message": "valid username"}, status=200)


class RegistrationView(View):
    def get(self, request):
        return render(request, "authentication/register.html")


class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")
