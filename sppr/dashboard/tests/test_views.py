from django.test import TestCase, Client
from django.urls import reverse
from dashboard.models import *

class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.profil_akl_url = reverse('profil', args=["akl"])
        self.login_url = reverse('login')
        self.login_auth = { 'username': 'admin', 'password': 'admin123' }
        self.form_akl_tujuan_url = reverse('addLfa', args=["tujuan"])
        self.form_akl_sasaran_url = reverse('addLfa', args=["sasaran"])
        self.form_akl_output_url = reverse('addLfa', args=["output"])

        self.test_view_login_POST() # Must login first prior to testing

        return super().setUp()

    def test_view_login_POST(self):
        login_response = self.client.post(self.login_url, self.login_auth)
        self.assertEquals(login_response.status_code, 302)

    def test_view_profil_akl_GET(self):
        get_response = self.client.get(self.profil_akl_url)
        provinsi_id = ProvinsiId.objects.all()

        self.assertEquals(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'profil/kerangka-logis.html')
        self.assertQuerysetEqual(get_response.context['provinsi'], provinsi_id, ordered=False)

    def test_view_profil_akl_POST(self):
        post_response = self.client.post(self.profil_akl_url, { 'pilih_provinsi': "11" })
        tujuans = TujuanLFA.objects.all().filter(provinsi_id=11)

        self.assertEquals(post_response.status_code, 200)
        self.assertQuerysetEqual(post_response.context['tujuans'], tujuans, ordered=False)