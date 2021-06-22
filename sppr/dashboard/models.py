from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Provinsi(models.Model):
    nama_provinsi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_provinsi


class Proyek(models.Model):
    provinsi = ForeignKey(Provinsi, on_delete=models.CASCADE)
    nama_proyek = models.CharField(max_length=1000)
    tahun_proyek = models.IntegerField()

    def __str__(self):
        return self.nama_proyek


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
