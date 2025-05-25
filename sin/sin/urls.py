from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('signup/', views.signup, name='signup'),
]
