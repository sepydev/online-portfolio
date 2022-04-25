from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View

from ..forms.register import RegisterForm

User = get_user_model()


class Register(View):
    template_name = './accounts/register.html'
    form = RegisterForm

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                'form': self.form
            }
        )

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            User.objects.create_user(
                clean_data['username'],
                clean_data['email'],
                clean_data['password'],
            )
            return redirect('core:home')

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )
