from django.shortcuts import render
from django.shortcuts import Http404
from .models import Endorsement

def landing(request):
    return render(request, 'dashboard/landing.html')

def masuk(request):
    return render(request, 'dashboard/login.html')

def dashboard(request):
    return render(request, 'dashboard/index.html')

def index(request):
    return render(request, 'dashboard/index.html')


def detail(request):
    try:
        question = Question.objects.get()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'dashboard/index.html',)


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


def profil(request, menu):

    judul = cek_profil(menu)

    return render(request, 'profil/index.html', {'judul': judul})


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


