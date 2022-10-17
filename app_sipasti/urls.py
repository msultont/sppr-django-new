from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index_sipasti"),
    path('albumtematik/', views.albumtematik, name="albumtematik"),
]
