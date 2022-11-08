# Generated by Django 3.2.14 on 2022-11-05 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_srupdt', '0003_alter_file_uploaded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_surat', models.DateTimeField()),
                ('nomor_surat', models.CharField(max_length=50)),
                ('judul_surat', models.CharField(max_length=300)),
                ('jenis_surat', models.CharField(choices=[('usulan', 'Penyampaian Usulan'), ('audiensi', 'Permohonan Audiensi')], max_length=50)),
                ('provinsi', models.CharField(choices=[('aceh', 'Aceh'), ('riau', 'Riau'), ('bengkulu', 'Bengkulu'), ('jawa Timur', 'Jawa Timur'), ('jambi', 'Jambi'), ('lampung', 'Lampung'), ('sumatera-selatan', 'Sumatera Selatan'), ('sumatera-barat', 'Sumatera Barat'), ('sumatera-utara', 'Sumatera Utara'), ('dki-jakarta', 'DKI Jakarta'), ('jawa-tengah', 'Jawa Tengah'), ('kepulauan-riau', 'Kepulauan Riau'), ('banten', 'Banten'), ('di-yogyakarta', 'DI Yogyakarta'), ('bangka-belitung', 'Bangka Belitung'), ('jawa-barat', 'Jawa Barat'), ('bali', 'Bali')], max_length=50)),
                ('kabupaten_kota', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='filehistory',
            name='file',
        ),
        migrations.RemoveField(
            model_name='filehistory',
            name='parent',
        ),
        migrations.DeleteModel(
            name='UsulanKlinik',
        ),
        migrations.DeleteModel(
            name='UsulanLanjut',
        ),
        migrations.DeleteModel(
            name='UsulanPemda',
        ),
        migrations.CreateModel(
            name='Audiensi',
            fields=[
                ('surat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_srupdt.surat')),
                ('nomenklatur_usulan', models.CharField(max_length=300)),
                ('target_usulan', models.TextField()),
                ('kebutuhan_anggaran', models.IntegerField()),
                ('indikasi_tahun_pembangunan', models.IntegerField()),
                ('lokasi_spesifik', models.CharField(max_length=50)),
                ('jenis_usulan', models.CharField(choices=[('infrastruktur', 'Infrastruktur'), ('non infrastruktur', 'Non infrastruktur')], max_length=100)),
                ('dasar_usulan', models.CharField(choices=[('audiensi', 'Audiensi'), ('surat', 'Surat')], max_length=20)),
                ('status_kesiapan_lahan', models.CharField(choices=[('siap', 'Siap'), ('belum siap', 'Belum siap'), ('tidak perlu', 'Tidak perlu')], max_length=20)),
                ('status_studi_persiapan', models.CharField(choices=[('pra fs', 'Pra FS'), ('fs', 'FS'), ('ded', 'DED')], max_length=20)),
                ('kewenangan', models.CharField(choices=[('pusat', 'Pusat'), ('daerah', 'Daerah')], max_length=20)),
                ('kementerian_lembaga_daerah', models.CharField(max_length=300)),
                ('sektor_bappenas', models.CharField(max_length=300)),
                ('kriteria_usulan', models.CharField(choices=[('usulan baru', 'Usulan Baru'), ('usulan lama', 'Usulan Lama')], max_length=100)),
                ('forum_perencanaan_diusulkan', models.BooleanField()),
                ('catatan_audiensi', models.TextField()),
                ('keterangan_tambahan', models.TextField()),
            ],
            bases=('app_srupdt.surat',),
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='FileHistory',
        ),
        migrations.CreateModel(
            name='PenelaahanAwal',
            fields=[
                ('audiensi_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_srupdt.audiensi')),
                ('ketersediaan_proyek_usulan', models.BooleanField()),
                ('terdapat_nomenklatur_usulan_yang_jelas', models.BooleanField()),
                ('terdapat_justifikasi_kebutuhan_usulan_proyek', models.BooleanField()),
                ('terdapat_identifikasi_kewenangan_pusatdaerah_dari_usulan_proyek', models.BooleanField()),
                ('memenuhi_kelengkapan_minimum_rediness_criteria', models.BooleanField()),
                ('rekomendasi_penelaahan_awal', models.CharField(choices=[('tidak direkomendasikan', 'Tidak Direkomendasikan'), ('dibahas lebih lanjut', 'Dibahas Lebih Lanjut')], max_length=100)),
            ],
            bases=('app_srupdt.audiensi',),
        ),
        migrations.CreateModel(
            name='KlinikKonsultasi',
            fields=[
                ('penelaahanawal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_srupdt.penelaahanawal')),
                ('catatan_pembahasan', models.TextField()),
                ('indikasi_sumber_pendanaan', models.CharField(max_length=200)),
                ('penelaahan_akhir', models.CharField(choices=[('tidak direkomendasikan', 'Tidak Direkomendasikan'), ('direkomendasikan', 'Direkomendasikan')], max_length=100)),
                ('surat_jawaban', models.CharField(max_length=200)),
                ('nodin_laporan', models.TextField()),
            ],
            bases=('app_srupdt.penelaahanawal',),
        ),
    ]
