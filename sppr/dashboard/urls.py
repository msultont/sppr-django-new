from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('home/', views.index, name='index'),

    # ex: /dashboard / 5
    path('<int:question_id>/', views.detail, name='detail'),

    # Akses untuk ke Menu Profil Daerah
    path('profil/<str:menu>', views.profil, name='profil'),

    # ex: /dashboard/10/vote
    # path('<int:question_id>/vote/', views.vote, name='vote')

    # Akses untuk ke Menu Kebutuhan Daerah
    path('kebdaerah/<str:menu>', views.kebdaerah, name='kebdaerah'),

    # Akses untuk ke Menu Proyek Mitra KL
    path('proyek/<str:menu>', views.proyek, name='proyek')




]
