from django import forms
from django.forms import ModelForm
from .models import CsvLongList, Longlist, OutputLFA, SasaranLFA, SkoringProyek, TujuanLFA, IsuStrategis, NewIsuStrategis

# Create form for Manipulate Longlist


class Output_LFA_Form(ModelForm):

    class Meta:
        model = OutputLFA
        fields = '__all__'

        widgets = {

            'nama_output': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Silahkan Isi Tujuan Disini'}),
            'sasaran': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'indikator': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'sumber_data': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'asumsi': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'}),
            'nilai': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'})

        }


class Sasaran_LFA_Form(ModelForm):

    class Meta:
        model = SasaranLFA
        fields = '__all__'

        widgets = {

            'nama_sasaran': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Silahkan Isi Tujuan Disini'}),
            'tujuan': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'indikator': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'sumber_data': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'asumsi': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'}),
            'nilai': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'})

        }


class Tujuan_LFA_Form(ModelForm):

    class Meta:
        model = TujuanLFA
        fields = '__all__'

        widgets = {

            'nama_tujuan': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Silahkan Isi Tujuan Disini'}),
            'provinsi': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'tahun': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'indikator': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'sumber_data': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Isi disini'}),
            'asumsi': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'}),
            'nilai': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Isi disini'})

        }


class IsuStrategisForm(ModelForm):

    class Meta:
        model = NewIsuStrategis
        fields = '__all__'

        widgets = {
            'provinsi': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'tahun': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'nama_isu': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'parent': forms.Select(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        }

class LonglistForm(ModelForm):

    class Meta:
        model = Longlist
        fields = '__all__'

        widgets = {

            'judul_proyek': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'provinsi': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'lokasi_kabupaten': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'lokasi_proyek': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'Contoh : Dekat pelabuhan X'}),
            'target_2021': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                    'placeholder': "Nilai, Unit Satuan"}),
            'indikasi_pendanaan_2021': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                'placeholder': "Dalam Rp. Juta"}),
            'target_2022': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                    'placeholder': "Nilai, Unit Satuan"}),
            'indikasi_pendanaan_2022': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                'placeholder': "Dalam Rp. Juta"}),
            'target_2023': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                    'placeholder': "Nilai, Unit Satuan"}),
            'indikasi_pendanaan_2023': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                'placeholder': "Dalam Rp. Juta"}),
            'target_2024': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                    'placeholder': "Nilai, Unit Satuan"}),
            'indikasi_pendanaan_2024': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                'placeholder': "Dalam Rp. Juta"}),
            'unit_satuan': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                  'placeholder': 'Contoh : Kilometer, Kilogram, Unit, Orang, Daerah...'}),
            'sumber_data': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'ket_sumber_data': forms.TextInput(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'kl_pelaksana': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'ket_kl_pelaksana': forms.TextInput(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'isu_strategis': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                    'placeholder': 'Contoh : Antisipasi Banjir, Rob, dan Genangan'}),
            'output_test': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'mp': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'status_usulan': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'taging_kawasan_prioritas': forms.Select(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'sumber_bahasan': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                     'placeholder': "Short-List/Prarakorgub/Musrenbangnas"}),
            'jenis_project': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'sub_tema_rkp': forms.TextInput(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'klasifikasi_proyek': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                         'placeholder': 'Isi klasifikasi proyek disini'}),
            'jenis_impact': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'staging_perkembangan': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'keterangan': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'shortlist_2022': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'shortlist_2023': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'usulan_baru': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'shortlist': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'prarakorgub': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'rakorgub': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'rakortekbang': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'musrenbangprov': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'musrenbangnas': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'endorsement': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'}),
            'tahun_longlist': forms.Select(attrs={'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500'})
        }

# Create form for edit DPP


class SkoringProyekForm(ModelForm):

    class Meta:
        model = SkoringProyek
        fields = ['nilai_raw_korelasi_sasaran', 'nilai_raw_korelasi_output',
                  'nilai_raw_MP', 'nilai_raw_investasi']

        widgets = {

            'nilai_raw_korelasi_sasaran': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                   'placeholder': "Nilai"}),
            'nilai_raw_korelasi_output': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                                  'placeholder': "Nilai"}),
            'nilai_raw_MP': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                     'placeholder': "Nilai"}),
            'nilai_raw_investasi': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                                                            'placeholder': "Nilai"})

        }

# Create form for upload CSV File


class CsvModelForm(ModelForm):
    class Meta:
        model = CsvLongList
        fields = ['file_name']
