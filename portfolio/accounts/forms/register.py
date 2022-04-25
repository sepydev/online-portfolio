from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    required_css_class = 'fv-row orm-label fw-bolder text-dark fs-6'
    job_title = forms.CharField(label='عنوان شغلی')
    password = forms.CharField(widget=forms.PasswordInput(), label='کلمه عبور')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='تایید کلمه عبور')

    class Meta:
        model = User
        fields = ('username', 'email', 'job_title', 'password', 'password_confirm',)
        labels = {
            'username': 'نام کاربری',
            'email': 'پست الکترونیک',
            'job_title': 'عنوان شغلی',
            'password': 'کلمه عبور',
            'password_confirm': 'تایید کلمه عبور',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg form-control-solid'
            })
            field.help_text = ""

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            raise forms.ValidationError("کلمه عبور و تایید کلمه عبور یکسان نمی باشد")

        return self.cleaned_data
