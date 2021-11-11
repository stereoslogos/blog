from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('signup/', views.register_page, name="signup"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]