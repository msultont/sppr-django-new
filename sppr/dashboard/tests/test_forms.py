from django.test import TestCase
from dashboard.forms import Tujuan_LFA_Form, Sasaran_LFA_Form, Output_LFA_Form

class TestForms(TestCase):
    def setUp(self):
        self.tujuan_form = Tujuan_LFA_Form(data={
            "nama_tujuan": "testing_tujuan_1",
            "provinsi": 11,
            "tahun": 2020,
            "indikator": "testing_tujuan_indikator_1",
            "sumber_data": "testing_tujuan_sumber_data_1",
            "asumsi": "testing_tujuan_asumsi_1",
            "nilai": 5.50
        })

        self.sasaran_form = Sasaran_LFA_Form(data={
            "tujuan": self.tujuan_form.save(), # create TujuanLFA model instance
            "nama_sasaran": "testing_sasaran_1",
            "indikator": "testing_sasaran_indikator_1",
            "sumber_data": "testing_sasaran_sumber_data_1",
            "asumsi": "testing_sasaran_asumsi_1",
            "nilai": 5.50,
            "pengaruh_sasaran_tujuan": 3.40
        })

        self.output_form = Output_LFA_Form(data={
            "sasaran": self.sasaran_form.save(), # create SasaranLFA model instance
            "nama_output": "testing_output_1",
            "indikator": "testing_output_indikator_1",
            "sumber_data": "testing_output_sumber_data_1",
            "asumsi": "testing_output)asumsi_1",
            "nilai": 5.50
        })

    def test_view_form_akl_create_tujuan_POST(self):
        tujuan_form = self.tujuan_form
        self.assertTrue(tujuan_form.is_valid())

    def test_view_form_akl_create_sasaran_POST(self):
        sasaran_form = self.sasaran_form

        self.assertTrue(sasaran_form.is_valid())

    def test_view_form_akl_create_output_POST(self):
        output_form = self.output_form

        self.assertTrue(output_form.is_valid())