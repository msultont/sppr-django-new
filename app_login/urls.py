from django.urls import path

from . import views

urlpatterns = [
    path('<str:stateargs>/', views.login, name='login'),
]
