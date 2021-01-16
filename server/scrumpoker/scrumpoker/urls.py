from django.contrib import admin
from django.urls import path
from poker import views

urlpatterns = [
    path('admin2021/', admin.site.urls),
    path('', views.home)
]
