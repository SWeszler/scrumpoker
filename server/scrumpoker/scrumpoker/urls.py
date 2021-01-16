from django.contrib import admin
from django.urls import path
from poker import views

urlpatterns = [
    path('admin2021/', admin.site.urls),
    path('get-logged-user/', views.get_logged_user),
    path('', views.home)
]
