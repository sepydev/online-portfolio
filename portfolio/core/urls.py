from django.urls import path

from .views import AdminPanel, Home

app_name = 'core'

urlpatterns = [
    path('admin-panel/', AdminPanel.as_view(), name='admin-panel'),
    path('', Home.as_view(), name='home'),
]
