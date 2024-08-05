from django.urls import path
from .views import login_view, logout_view, home, register, account

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('', home, name='home')
    
]