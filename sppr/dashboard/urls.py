from django.urls import path

from . import views

urlpatterns = [

    # ex: /landing 
    path('', views.landing, name='landing'),

    # ex: /halaman login page
    path('dashboard/login', views.masuk, name='masuk'),

    # ex: /dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/index', views.dashboard, name='dashboard'),

    # ex: /dashboard / 5
    path('<int:question_id>/', views.detail, name='detail'),

    # Akses untuk ke Menu Profil Daerah
    path('profil/<str:menu>', views.profil, name='profil'),

    # ex: /dashboard/10/vote
    # path('<int:question_id>/vote/', views.vote, name='vote')

    # Akses untuk ke Menu Kebutuhan Daerah
    path('kebdaerah/<str:menu>', views.kebdaerah, name='kebdaerah'),





]
