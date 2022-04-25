from django import forms


class LoginForm(forms.Form):
    required_css_class = 'fv-row orm-label fw-bolder text-dark fs-6'
    attrs = {
        'class': 'form-control form-control-lg form-control-solid'
    }
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(label='کلمه عبور', widget=forms.PasswordInput(attrs=attrs))
