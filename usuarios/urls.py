from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),
]