from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from ..forms.login import LoginForm

User = get_user_model()


class Login(View):
    template_name = './accounts/login.html'
    form = LoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            username = clean_data['username']
            password = clean_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('core:home')
            messages.error(request, 'نام کاربری یا کلمه عبور صحیح نمی باشد', 'danger')
        return render(request, self.template_name, {'form': self.form})
