from django.db import models
from django.shortcuts import render
from django.shortcuts import Http404
from .models import Endorsement
from django.db.models import Count
from django.http import JsonResponse
# from django_serverside_datatable.views import ServerSideDatatableView
from ajax_datatable.views import AjaxDatatableView
# from django_datatables_view.base_datatable_view import BaseDatatableView


# class ItemListView(ServerSideDatatableView):
#     queryset = Endorsement.objects.all()
#     columns = ['id', 'provinsi', 'nama_kegiatan',
#                'lokasi', 'ki', 'status_approval']


class EndorsementDataView(AjaxDatatableView):

    model = Endorsement
    title = 'Endorsement'
    initial_order = [["id", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, 'title': 'No'},
        {'name': 'provinsi', 'title': 'Provinsi', 'foreign_field': 'provinsi__nama_provinsi',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'nama_kegiatan', 'visible': True, 'title': 'Nama Kegiatan'},
        {'name': 'ki_id', 'foreign_field': 'ki__nama_kementrian_lembaga', 'title': 'Kementrian Lembaga',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'status_approval', 'visible': True,
            'choices': True, 'autofilter': True}
    ]


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'auth/login.html')


def dashboard(request):
    return render(request, 'dashboard/index.html')


# def detail(request):
#     try:
#         question = Question.objects.get()
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'dashboard/index.html',)


def cek_profil(menu):

    if menu == "ku":
        judul = "Kondisi Umum Wilayah"
    elif menu == "pis":
        judul = "Permasalahan Isu Strategis"
    elif menu == "akl":
        judul = "Analisis Kerangka Logis"
    elif menu == "akp":
        judul = "Analisis Kawasan Prioritas"
    else:
        judul = "Kesalahan Memilih Menu"

    return judul


def cek_kebdaerah(menu):

    if menu == "longlist":
        judul = "Daftar Panjang Proyek"
    elif menu == "prioritas":
        judul = "Daftar Proyek Prioritas"
    elif menu == "forum":
        judul = "Catatan Kesepakatan Forum perencanaan"
    elif menu == "prakorgub":
        judul = "Pra Rapat Koordinasi Gubernur"
    elif menu == "rakorgub":
        judul = "Rapat Koordinasi Gubernur"
    elif menu == "rakortekrenbang":
        judul = "Rapat Koordinasi Teknis Pembangunan"
    elif menu == "musrenbangnas":
        judul = "Musyawarah Pembangunan Nasional"
    else:
        judul = "Kesalahan Memilih Menu"

    return judul


def cek_proyek(menu):

    if menu == "batam":
        judul = "BP Batam"
    elif menu == "sabang":
        judul = "BPK Sabang"

    return judul


def profil(request, menu):

    judul = cek_profil(menu)

    return render(request, 'profil/index.html', {'judul': judul})


def chart_ro(request):

    labels = []
    data = []
    ro_by_kl = Endorsement.objects.values(
        'ki_id__nama_kementrian_lembaga').annotate(jumlah=Count('nama_kegiatan'))

    for row in ro_by_kl:
        labels.append(row['ki_id__nama_kementrian_lembaga'])
        data.append(row['jumlah'])

    data = {
        'labels': labels,
        'data': data
    }

    return JsonResponse(data)


def chart_prov(request):

    labels = []
    data = []
    ro_by_prov = Endorsement.objects.values(
        "provinsi_id__nama_provinsi").annotate(jumlah=Count('nama_kegiatan'))

    for row in ro_by_prov:
        labels.append(row["provinsi_id__nama_provinsi"])
        data.append(row['jumlah'])

    data = {
        'labels': labels,
        'data': data
    }

    return JsonResponse(data)


def kebdaerah(request, menu):

    sub_menu = ""
    judul = cek_kebdaerah(menu)
    content = {}

    if menu in ["longlist", "prioritas"]:
        sub_menu = "list"
        model = Endorsement
        field_names = [f.name for f in model._meta.get_fields()]
        endorsement_list = Endorsement.objects.all()

        content["data"] = endorsement_list
        content["fields"] = field_names

    elif menu in ["forum"]:
        sub_menu = "ckfp"
    elif menu in ["prakorgub", "rakorgub", "rakortekrenbang", "musrenbangnas"]:
        sub_menu = "tahapan"
    else:
        sub_menu = "error"

    content["judul"] = judul

    return render(request, f'kebutuhan_daerah/{sub_menu}.html', content)


def proyek(request, menu):

    judul = cek_proyek(menu)

    return render(request, 'proyek/index.html', {'judul': judul})
