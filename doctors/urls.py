from django.urls import path
from . import views
from .views import register_doctor


urlpatterns = [
    path('', views.index, name='index'),
    # path("<int:id>", views.index, name='index'),
    path('home', views.home, name='home'),
    path('register_user', views.register_user, name='register_user'),
    path('my-login', views.login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register_doctor', views.register_doctor, name='register_doctor'),
]