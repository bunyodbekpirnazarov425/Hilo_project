from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout

from app.forms import RegisterForm, LoginForm


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

class RegisterView(View):
    def get(self, request):
        context = {
            'title': "Register",
            'image_url': "https://avatars.mds.yandex.net/i?id=68b79a3a541ebe243674b173c63c2fc3_l-10310748-images-thumbs&n=13"
        }
        return render(request, "register.html", context)

    def post(self, request: WSGIRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Saytdan muaffaqiyatli ro'yxatdan o'tdingiz {user.username} \n"
                                                f"Login parolni terib saytga krishingiz mumkin!")
            return redirect('home')
        return redirect('register')

class LoginView(View):
    def get(self, request):
        context = {
            'title': "Login",
            'image_url': "https://avatars.mds.yandex.net/i?id=68b79a3a541ebe243674b173c63c2fc3_l-10310748-images-thumbs&n=13"
        }
        return render(request, "login.html")

    def post(self, request: WSGIRequest):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user = form.save()
            messages.success(request, f"Saytga xush kelibsiz {user.username}")
            return redirect('home')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.error(request, "Siz saytdan chiqib ketdingiz!!! \n"
                        "Kirish uchun login parolingizni kiriting!!")
        return redirect('login')