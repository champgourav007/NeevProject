from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.accountView, name="account"),
    path('signup/', views.signupView, name="signup"),
    path('signin/', views.loginView, name="signin"),
]
