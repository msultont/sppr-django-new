import json
from django.shortcuts import render


def getData():
    province_list = ['Aceh',
                     'Sumatera Utara',
                     'Sumatera Barat',
                     'Riau',
                     'Jambi',
                     'Sumatera Selatan',
                     'Bengkulu',
                     'Lampung',
                     'Kep. Bangka Belitung',
                     'Kep. Riau',
                     'DKI Jakarta',
                     'Jawa Barat',
                     'Jawa Tengah',
                     'DI Yogyakarta',
                     'Jawa Timur',
                     'Banten',
                     'Bali']

    dummyData = [{
                    "tittle": "Kemacetan Ulapan",
                    "img": "https://www.baliaround.com/wp-content/uploads/2013/09/monkey-forest-ubud.jpg",
                    "text": "Analisis kebutuhan infrastruktur transportasi dalam mengatasi isu dan permasalahan kemacetan, kurangnya lahan parkir, minimnya layanan transportasi umum berdasarkan dokumen perencanaan yang ada, seperti Rencana Aksi dalam Rencana Induk Terpadu (Integrated Master Plan) Pengembangan Kawasan Pariwisata Ulapan.",
                    "province": "Bali"
                 },
                 {
                    "tittle": "Pelabuhan Industri Lampung",
                    "img": "https://logisklik.com/blog/wp-content/uploads/2022/05/panjang2.jpg",
                    "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    "province": "Lampung"
                 },
                 {
                    "tittle": "Geopark Karangsambung",
                    "img": "https://www.goodnewsfromindonesia.id/uploads/images/2020/07/2115342020-Goodnewsfromindonesia-GNFI-Sungai-Luk-Ulo.jpg",
                    "text": "Geopark atau taman bumi merupakan sebuah wilayah geografi tunggal atau gabungan, yang memiliki situs warisan geologi(geosite) dan bentang alam yang bernilai, terkait aspek warisan geologi, keanekaragaman geologi, hayati dan budaya.",
                    "province": "Jawa Tengah"
                 },
                 {
                    "tittle": "Isu Strategis: Tingginya resiko bencana di pantura jawa tengah",
                    "img": "https://i.ytimg.com/vi/5Ee_8hXCur8/maxresdefault.jpg",
                    "text": "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                    "province": "Jawa Tengah"
                 }]

    return {"a": province_list, "b": dummyData}


def index(request):
    return render(request, "index_sipasti.html")


def albumtematik(request):
    data = getData()
    return render(request, "albumtematik/albumtematik.html", {"province": json.dumps(data['a']),
                                                              "contentD": json.dumps(data['b'])})
