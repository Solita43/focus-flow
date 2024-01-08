from django.urls import path
from . import views

urlpatterns = [
    path("register", views.SignUpView.as_view()),
    path("login", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("csrf_cookie", views.GetCSRFToken.as_view()),
]
