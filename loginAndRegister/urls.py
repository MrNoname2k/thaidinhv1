from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.goLogin,name='login'),
    path('register/', views.goRegister,name='register'),
]
