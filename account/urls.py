from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'


urlpatterns = [
    # собственное представление входа
    # path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', register_view, name='register'),

    path('', views.dashboard, name='dashboard'),

]