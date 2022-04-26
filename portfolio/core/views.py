from django.shortcuts import render
from django.views import View


class AdminPanel(View):
    def get(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            profile = request.user.profile
        else:
            profile = None
        return render(request, 'core/admin-panel.html', {'profile': profile})


class Home(View):
    def get(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            profile = request.user.profile
        else:
            profile = None
        return render(request, 'core/home.html', {'profile': profile})
