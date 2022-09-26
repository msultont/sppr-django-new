from django.urls import path

from . import views

urlpatterns = [
    path('<str:_state>/', views.login, name='login'),
]
