from django.urls import path
from . import views

urlpatterns = [

    # Akses ke halaman landing page
    path('', views.index, name='index'),

    # Akses ke halaman login
    path('auth/login', views.login, name='login'),

    # Akses ke dashboard utama
    path('dashboard/', views.dashboard, name='dashboard'),

    # Akses untuk ke Menu Profil Daerah
    path('profil/<str:menu>', views.profil, name='profil'),

    # Akses untuk ke Menu Kebutuhan Daerah
    path('kebdaerah/<str:menu>', views.kebdaerah, name='kebdaerah'),

    # Akses untuk ke menu proyek mitra KL
    path('proyek/<str:menu>', views.proyek, name="proyek"),

    path('rochart/', views.chart_ro, name='rochart'),

    path('provchart/', views.chart_prov, name='provchart'),
    # path('data/', views.ItemListView.as_view()),
    path('ajax_datatable/permissions/', views.EndorsementDataView.as_view(),
         name="ajax_datatable_permissions"),

    # path to form endorsement
    path('forms/endorsement/add', views.addEndorsement, name="addEndorsement"),
    path('forms/endorsement/update/<int:pk>',
         views.updateEndorsement, name="updateEndorsement")

]
