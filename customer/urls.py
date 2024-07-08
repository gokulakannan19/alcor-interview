from django.urls import path
from . import views


urlpatterns = [
    path('', views.extract_user_info)
]