from os import name
from django.urls import path
from . import views

urlpatterns = [

    # Akses ke halaman landing page
    path('', views.index, name='index'),

    # Akses ke halaman login
    path('auth/login', views.loginUser, name='login'),
    path('auth/logout', views.logoutUser, name='logout'),

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

    # Path to Longlist Data View
    path('ajax_datatable/longlist', views.LonglistDataView.as_view(),
         name="longlist"),

    # Path to CRUD Longlist
    path('forms/longlist/add', views.addSingleLonglist,
         name="addSingleLonglist"),
    path('forms/longlist/update/<int:pk>',
         views.updateLonglist, name="updateLonglist"),
    path('forms/longlist/delete/<int:pk>',
         views.deleteSingleLonglist, name="deleteSingleLonglist"),

    # Path to download excel longlist data format
    path('download/format/longlist/',
         views.download_longlist_format, name="downloadLonglist")

]
