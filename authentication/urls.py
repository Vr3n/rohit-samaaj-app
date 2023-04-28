from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, logout_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),

    # Change Password.
    path("change-password/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change_form.html",
    ), name="change_password"),

    # Forgot Password.
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset_form.html",
         ), name="password_reset"),

    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html",
    ), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_confirm.html"
         ),
         name="password_reset_confirm"
         ),

    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_complete.html",
         ),
         name="password_reset_complete",
         )


]
