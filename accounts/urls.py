from django.urls import path
from . import views
from django.contrib.auth import views as log_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', log_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', log_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password-reset/',log_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password-reset/done/', log_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),path('password-reset-confirm/<uidb64>/<token>/', log_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',log_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    
]

