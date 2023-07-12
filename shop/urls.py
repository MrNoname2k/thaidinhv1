from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.goHome,name='home'),
    path('home/', views.goHome,name='home'),
    path('logout/', views.logout, name="logout"),
    path('item/<int:id>/',views.getItem, name="item"),   
]
