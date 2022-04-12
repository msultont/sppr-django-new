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
    path('profil/<str:menu>/', views.profil, name='profil'),

    # Akses untuk ke Menu Kebutuhan Daerah
    path('kebdaerah/<str:menu>', views.kebdaerah, name='kebdaerah'),

    # Akses untuk ke Menu Kajian Kewilayahan
    path('kajian/', views.kajian_wilayah, name="kawil"),

    path('monev_spasial/', views.monev_spasial, name="monev_spasial"),

    # Akses untuk ke menu proyek mitra KL
    path('proyek/<str:menu>', views.proyek, name="proyek"),

    path('rochart/', views.chart_ro, name='rochart'),

    path('provchart/', views.chart_prov, name='provchart'),
    # path('data/', views.ItemListView.as_view()),

    # Akses untuk API di Kondisi Umum Wilayah
    path('apikuw/', views.api_kuw, name='apikuw'),

    # Path to Longlist Data View
    path('ajax_datatable/longlist', views.LonglistDataView.as_view(),
         name="longlist"),

    # Path to Endorsement Data View
    path('ajax_datatable/endorsement', views.EndorsementDataView.as_view(),
         name="endorsement"),

    # Path Hasil Skoring Data View
    path('ajax_datatable/skoring_lfa', views.HasilSkoringDataView.as_view(),
         name="skoring_lfa"),

    # Path to Kesepakatan Forum Data View

    path('ajax_datatable/kesepakatan-forum',
         views.KesepakatanForumDataView.as_view(), name="kesepakatan-forum"),

    # Path to Kawasan Prioritas Data View
    path('ajax_datatable/kawasan-prioritas',
         views.KawasanPrioritasDataView.as_view(), name="kawasan-prioritas"),

    # Path to CRUD Longlist
    path('forms/longlist/add', views.addSingleLonglist,
         name="addSingleLonglist"),
    path('forms/longlist/update/<int:pk>',
         views.updateLonglist, name="updateLonglist"),
    path('forms/longlist/delete/<int:pk>',
         views.deleteSingleLonglist, name="deleteSingleLonglist"),

    # Path to CRUD Isu Strategis
    path('forms/isu_strategis/add',
         views.addIsuStrategis, name='addIsu'),

    # Path to CRUD Skoring
    path('forms/skoring/update/<int:pk>',
         views.updateHasilSkoring, name="updateSkoring"),

    # Path to CRUD LFA
    path('forms/add_lfa/<str:tipe>',
         views.addkerangkalogis, name='addLfa'),

    # Path to download excel longlist data format
    path('download/format/longlist/',
         views.download_longlist_format, name="downloadLonglist"),
]