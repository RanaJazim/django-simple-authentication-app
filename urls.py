from django.urls import path
from authapp import views
from django.contrib.auth.views import LoginView

app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='authapp/login.html'),
         name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('password-change/', views.password_change, name='password_change'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
]