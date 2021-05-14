from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name="user/login.html"), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(), name="signout"),
    path('signup/', views.register, name='signup')
]
