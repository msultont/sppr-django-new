from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count, query
from django.http import JsonResponse
from ajax_datatable.views import AjaxDatatableView
from .forms import CsvModelForm, LonglistForm, SkoringProyekForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
from distutils import util
import os
import mimetypes
from django.http.response import HttpResponse


"""

    User Authentication

"""
# User Login


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

        return render(request, 'auth/login.html')

# User Logout


def logoutUser(request):
    logout(request)
    return redirect('index')

############################


"""

    Routing

"""
# Route to Landing Page


def index(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'index.html')

# Route to Dashboard Main Page


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/index.html')

# Route to Profil Daerah Page


@login_required(login_url='login')
def profil(request, menu):

    judul = cek_profil(menu)
    template = cek_profil_template(menu)

    return render(request, f'profil/{template}.html', {'judul': judul})

# Route to Kebutuhan Daerah Page


@login_required(login_url='login')
def kebdaerah(request, menu):

    sub_menu = ""
    dataView = ""
    chartDataView = ""
    judul = cek_kebdaerah(menu)
    content = {}
    status_upload = ""

    if menu == "longlist":
        dataView = "longlist"
        chartDataView = "longlistChartView"
        form = CsvModelForm(request.POST or None, request.FILES or None)

        try:
            if form.is_valid():
                row_uploaded = 0
                obj = form.save()

                # Read data from csv

                with open(obj.file_name.path, 'r') as f:
                    reader = csv.reader(f)

                    for i, row in enumerate(reader):
                        if i == 0:
                            pass
                        elif row[2] == "":
                            pass
                        else:
                            Longlist.objects.create(
                                judul_proyek=row[2],
                                provinsi=ProvinsiId(
                                    provinsi_id=int(row[1])),
                                lokasi_kabupaten=KabupatenId(
                                    kabupaten_id=int(row[4])),
                                lokasi_proyek=row[5],
                                target_2021=float(row[6]),
                                target_2022=float(row[7]),
                                target_2023=float(row[8]),
                                target_2024=float(row[9]),
                                target_2025=float(row[10]),
                                unit_satuan=row[11],
                                # indikasi_pendanaan_2021=float(row[12]),
                                # indikasi_pendanaan_2022=float(row[13]),
                                # indikasi_pendanaan_2023=float(row[14]),
                                # indikasi_pendanaan_2024=float(row[15]),
                                sumber_data=SumberdataId(
                                    sumberdata_id=int(row[17])),
                                ket_sumber_data=row[18],
                                kl_pelaksana=KlId(kl_id=int(row[20])),
                                ket_kl_pelaksana=row[21],
                                shortlist_2022=bool(
                                    util.strtobool(row[22])),
                                shortlist_2023=bool(
                                    util.strtobool(row[23])),
                                isu_strategis=row[24],
                                tujuan_lfa=row[25],
                                sasaran_lfa=row[26],
                                output_lfa=row[27],
                                mp=MajorprojectId(mp_id=int(row[29])),
                                status_usulan=StatusId(
                                    status_id=int(row[31])),
                                sumber_bahasan=row[32],
                                taging_kawasan_prioritas=KawasanprioritasId(
                                    kp_id=int(row[34])),
                                prioritas_tahun_2022=row[35],
                                prioritas_tahun_2023=row[36],
                                prioritas_tahun_2024=row[37],
                                jenis_project=ProyekId(
                                    proyek_idd=int(row[39])),
                                sub_tema_rkp=row[40],
                                klasifikasi_proyek=row[41],
                                jenis_impact=row[42],
                                staging_perkembangan=row[43],
                                keterangan=row[44],
                                usulan_baru=bool(
                                    util.strtobool(row[45])),
                                shortlist=bool(
                                    util.strtobool(row[46])),
                                prarakorgub=bool(
                                    util.strtobool(row[47])),
                                rakorgub=bool(
                                    util.strtobool(row[48])),
                                rakortekbang=bool(
                                    util.strtobool(row[49])),
                                musrenbangprov=bool(
                                    util.strtobool(row[50])),
                                musrenbangnas=bool(
                                    util.strtobool(row[51])),
                                endorsement=bool(
                                    util.strtobool(row[52]))

                            )
                            row_uploaded += 1

                # content[status_upload] = f'Berhasil Mengunggah {row_uploaded} Objek Data.'
                return redirect('/kebdaerah/longlist', content)

        except:
            content['status_upload'] = f'Terdapat Kesalahan Dalam Mengunggah Data. Cek Kembali Format Data.'
            return redirect('/kebdaerah/longlist', content)

        content = {'form': form}
        sub_menu = "longlist"

    elif menu == "prioritas":
        dataView = "skoring_lfa"
        chartDataView = "endoresementChartView"
        sub_menu = "endorsement"

    elif menu == "forum":
        dataView = "kesepakatan-forum"
        sub_menu = "ckfp"

    elif menu == "logis":
        sub_menu = "kerangka-logis"

    else:
        sub_menu = "error"

    content["judul"] = judul
    content["dataView"] = dataView

    return render(request, f'kebutuhan_daerah/{sub_menu}.html', content)

# Route to Proyek Daerah Page


@login_required(login_url='login')
def proyek(request, menu):

    judul = cek_proyek(menu)

    return render(request, 'proyek/index.html', {'judul': judul})

# Route to Kajian Kewilayahan


@login_required(login_url="login")
def kajian_wilayah(request):

    return render(request, 'kajian_wilayah/index.html')

############################


"""

    Routing Support

"""


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


def cek_profil_template(menu):
    template = ""
    if menu == "ku":
        template = "index"
    elif menu == "pis":
        template = "isu-strategis"
    elif menu == "akl":
        template = "kerangka-logis"
    elif menu == "akp":
        template = "kawasan-prioritas"

    return template


def cek_kebdaerah(menu):

    if menu == "longlist":
        judul = "Daftar Panjang Proyek"
    elif menu == "prioritas":
        judul = "Daftar Proyek Prioritas"
    elif menu == "forum":
        judul = "Catatan Kesepakatan Forum perencanaan"
    elif menu == "logis":
        judul = "Hasil Analisis Kerangka Logis"
    else:
        judul = "Kesalahan Memilih Menu"

    return judul


def cek_proyek(menu):

    if menu == "batam":
        judul = "BP Batam"
    elif menu == "sabang":
        judul = "BPK Sabang"

    return judul

############################


"""

    Longlist

"""

# Retrieve Long List Data


class LonglistDataView(AjaxDatatableView):
    model = Longlist
    title = 'Longlist'
    initial_order = [["judul_proyek", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        {'name': 'pk', 'visible': False, 'title': 'No'},
        {'name': 'judul_proyek', 'visible': True, 'title': 'Judul Proyek'},
        {'name': 'provinsi', 'title': 'Provinsi', 'foreign_field': 'provinsi__nama_provinsi',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'isu_strategis', 'visible': True, 'title': 'Isu Strategis'},
        {'name': 'kl_pelaksana', 'foreign_field': 'kl_pelaksana__nama', 'title': 'Kementrian Lembaga',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'sumber_data', 'foreign_field': 'sumber_data__nama_sumber', 'title': 'Sumber Data',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'status_usulan', 'foreign_field': 'status_usulan__nama_status', 'visible': True,
            'choices': True, 'autofilter': True},
        {'name': 'taging_kawasan_prioritas', 'title': 'Taging Kawasan', 'foreign_field': 'taging_kawasan_prioritas__kawasan_prioritas',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'edit', 'title': 'Action', 'placeholder': True,
         'searchable': False, 'orderable': False, },
        {'name': 'lokasi_proyek', 'visible': False},
        {'name': 'target_2021', 'visible': False},
        {'name': 'target_2022', 'visible': False},
        {'name': 'target_2023', 'visible': False},
        {'name': 'target_2024', 'visible': False},
        {'name': 'target_2025', 'visible': False},
        {'name': 'indikasi_pendanaan_2021', 'visible': False},
        {'name': 'indikasi_pendanaan_2022', 'visible': False},
        {'name': 'indikasi_pendanaan_2023', 'visible': False},
        {'name': 'indikasi_pendanaan_2024', 'visible': False},
        {'name': 'tujuan_lfa', 'visible': False},
        {'name': 'sasaran_lfa', 'visible': False},
        {'name': 'output_lfa', 'visible': False},
        {'name': 'keterangan', 'visible': False},
    ]

    def customize_row(self, row, obj):
        row['edit'] = """
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" 
            onclick=" 
            var id = this.closest('tr').id.substr(4); location.replace('/forms/longlist/update/'+id);">
               Edit
            </button>
        """


# Retrieve Endorsement List Data

class EndorsementDataView(AjaxDatatableView):

    model = Longlist
    title = 'Endorsement'

    initial_order = [["judul_proyek", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        {'name': 'pk', 'visible': False, 'title': 'No'},
        {'name': 'judul_proyek', 'visible': True, 'title': 'Judul Proyek'},
        {'name': 'provinsi', 'title': 'Provinsi', 'foreign_field': 'provinsi__nama_provinsi',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'isu_strategis', 'visible': True, 'title': 'Isu Strategis'},
        {'name': 'kl_pelaksana', 'foreign_field': 'kl_pelaksana__nama', 'title': 'Kementrian Lembaga',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'sumber_data', 'foreign_field': 'sumber_data__nama_sumber', 'title': 'Sumber Data',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'status_usulan', 'foreign_field': 'status_usulan__nama_status', 'visible': True,
            'choices': True, 'autofilter': True},
        {'name': 'taging_kawasan_prioritas', 'title': 'Taging Kawasan', 'foreign_field': 'taging_kawasan_prioritas__kawasan_prioritas',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'edit', 'title': 'Action', 'placeholder': True,
         'searchable': False, 'orderable': False, }
    ]

    def get_initial_queryset(self, request=None):
        queryset = self.model.objects.filter(endorsement=True)
        return queryset

    def customize_row(self, row, obj):
        row['edit'] = """
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" 
            onclick=" 
            var id = this.closest('tr').id.substr(4); location.replace('/forms/longlist/update/'+id);">
               Edit
            </button>
        """

# Retrieve Hasil Skoring


class HasilSkoringDataView(AjaxDatatableView):

    model = SkoringProyek
    title = 'Hasil Skoring Proyek'

    initial_order = [["proyek", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, 'title': 'No'},
        {'name': 'proyek', 'visible': True, 'title': 'Judul Proyek',
            'foreign_field': 'proyek__judul_proyek'},
        {'name': 'nilai_raw_korelasi_sasaran',
            'title': 'Nilai Korelasi Sasaran', 'visible': True},
        {'name': 'nilai_raw_korelasi_output',
            'title': 'Nilai Korelasi Output', 'visible': True},
        {'name': 'nilai_raw_MP',
            'title': 'Nilai MP', 'visible': True},
        {'name': 'nilai_raw_investasi',
         'title': 'Nilai Investasi', 'visible': True},
        {'name': 'total_skoring', 'title': 'Hasil Skoring', 'visible': True},
        {'name': 'edit', 'title': 'Action', 'placeholder': True,
         'searchable': False, 'orderable': False}

    ]

    def get_initial_queryset(self, request=None):
        queryset = self.model.objects.filter(proyek__shortlist=True)
        return queryset

    def customize_row(self, row, obj):
        row['edit'] = """
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" 
            onClick="
            var id = this.closest('tr').id.substr(4); 
            location.replace('/forms/skoring/update/'+id);">
            Edit
            </button>
        """


# Retrieve Kesepakatan Forum List Data


class KesepakatanForumDataView(AjaxDatatableView):

    model = Longlist
    title = 'Catatan Kesepakatan Forum Perencanaan'

    initial_order = [["judul_proyek", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        {'name': 'pk', 'visible': False, 'title': 'No'},
        {'name': 'judul_proyek', 'visible': True, 'title': 'Judul Proyek'},
        {'name': 'provinsi', 'title': 'Provinsi', 'foreign_field': 'provinsi__nama_provinsi',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'isu_strategis', 'visible': True, 'title': 'Isu Strategis'},
        {'name': 'kl_pelaksana', 'foreign_field': 'kl_pelaksana__nama', 'title': 'Kementrian Lembaga',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'sumber_data', 'foreign_field': 'sumber_data__nama_sumber', 'title': 'Sumber Data',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'status_usulan', 'foreign_field': 'status_usulan__nama_status', 'visible': True,
            'choices': True, 'autofilter': True},
        {'name': 'taging_kawasan_prioritas', 'title': 'Taging Kawasan', 'foreign_field': 'taging_kawasan_prioritas__kawasan_prioritas',
            'visible': True, 'choices': True, 'autofilter': True},
        {'name': 'edit', 'title': 'Action', 'placeholder': True,
         'searchable': False, 'orderable': False, }
    ]

    def get_initial_queryset(self, request=None):
        queryset = self.model.objects.filter(
            shortlist=True, prarakorgub=True, rakorgub=True, rakortekbang=True, musrenbangprov=True, musrenbangnas=True)
        return queryset

    def customize_row(self, row, obj):
        row['edit'] = """
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" 
            onclick=" 
            var id = this.closest('tr').id.substr(4); location.replace('/forms/longlist/update/'+id);">
               Edit
            </button>
        """

# Retrieve Kawasan Prioritas List Data


class KawasanPrioritasDataView(AjaxDatatableView):

    model = DataKawasanPrioritas
    title = 'Skoring Kawasan Prioritas'

    initial_order = [["id", "asc"], ]
    length_menu = [[20, 50, 100, -1], [20, 50, 100, 'all']]
    search_values_separator = ' '

    column_defs = [
        {'name': 'id', 'visible': True, 'title': 'No'},
        {'name': 'nama_kawasan_prioritas',
            'visible': True, 'title': 'Kawasan Prioritas'},
        {'name': 'perencanaan', 'visible': True, 'title': 'Perencanaan'},
        {'name': 'kesiapan_kawasan', 'visible': True, 'title': 'Kesiapan Kawasan'},
        {'name': 'potensi_konektivitas', 'visible': True,
            'title': 'Potensi Konektivitas'},
        {'name': 'dampak_ekonomi', 'visible': True, 'title': 'Dampak Ekonomi'},
        {'name': 'dampak_lingkungan', 'visible': True, 'title': 'Dampak Lingkungan'},
        {'name': 'risiko_bencana', 'visible': True, 'title': 'Risiko Bencana'},
        {'name': 'total_nilai', 'visible': True, 'title': 'Total Nilai'},
        {'name': 'dampak_ekonomi_revisi', 'visible': True,
            'title': 'Dampak Ekonomi Revisi'},
        {'name': 'kawasan_prioritas', 'visible': True, 'title': 'Kawasan Prioritas'},
    ]

# Create Single Long List Data


@login_required(login_url='login')
def addSingleLonglist(request):
    form = LonglistForm()
    content = {'judul': "Anda Sedang Menambah Data Longlist"}

    if request.method == 'POST':
        form = LonglistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kebdaerah/longlist')

    content["form"] = form

    return render(request, 'forms/longlist.html', content)

# Update Single Long List Data


@login_required(login_url='login')
def updateLonglist(request, pk):

    longlist = Longlist.objects.get(id=pk)
    form = LonglistForm(instance=longlist)
    content = {'form': form,
               'judul': "Anda Sedang Memperbaharui Data Longlist", 'pk': pk}

    if request.method == 'POST':
        form = LonglistForm(request.POST, instance=longlist)
        if form.is_valid():
            form.save()
            return redirect('/kebdaerah/longlist')

    return render(request, 'forms/longlist.html', content)

# Delete Single Long List Data


@login_required(login_url='login')
def deleteSingleLonglist(request, pk):

    longlist = Longlist.objects.get(id=pk)

    longlist.delete()
    return redirect('/kebdaerah/longlist')

# Download Long List Data CSV Format

# Update Hasil Skoring


@login_required(login_url='login')
def updateHasilSkoring(request, pk):
    proyek = SkoringProyek.objects.get(id=pk)
    form = SkoringProyekForm(instance=proyek)

    content = {'form': form,
               'judul': "Anda Sedang Memperbaharui Hasil Skoring Proyek", 'pk': pk,
               'proyek': proyek
               }

    if request.method == 'POST':
        form = SkoringProyekForm(request.POST, instance=proyek)
        if form.is_valid():
            form.save()
            return redirect('/kebdaerah/prioritas')

    return render(request, 'forms/dpp-update.html', content)


def download_longlist_format(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Longlist Format Database.xlsx'
    # Define the full file path
    filepath = BASE_DIR + '/Format_Database/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

# Chart Kementrian Lembaga Pelaksana


def chart_ro(request):

    labels = []
    data = []
    ro_by_kl = Longlist.objects.values(
        'kl_pelaksana__singkatan').annotate(jumlah=Count('judul_proyek'))

    for row in ro_by_kl:
        labels.append(row['kl_pelaksana__singkatan'])
        data.append(row['jumlah'])

    data = {
        'labels': labels,
        'data': data
    }

    return JsonResponse(data)

# Chart Status Usulan


def chart_prov(request):

    labels = []
    data = []
    ro_by_prov = Longlist.objects.values(
        'status_usulan__nama_status').annotate(jumlah=Count('judul_proyek'))

    for row in ro_by_prov:
        labels.append(row["status_usulan__nama_status"])
        data.append(row['jumlah'])

    data = {
        'labels': labels,
        'data': data
    }

    return JsonResponse(data)


############################
