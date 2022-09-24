from django.contrib.auth.models import AbstractUser
from django.db import models

#   * Custom Authentication Model


ROLE_CHOICE = (
    ('developer', 'Developer'),
    ('director', 'Director'),
    ('secretary', 'Secretary'),
    ('coordinator', 'Coordinator'),
    ('pic', 'PIC'),
)

APP_CHOICE = (
    ('sppr', 'SPPR'),
    ('srupdt', 'SRUPDT'),
)


PIC_CHOICE = (
    ('aceh', 'Aceh'),
    ('riau', 'Riau'),
    ('bengkulu', 'Bengkulu'),
    ('jawa Timur', 'Jawa Timur'),
    ('jambi', 'Jambi'),
    ('lampung', 'Lampung'),
    ('sumatera-selatan', 'Sumatera Selatan'),
    ('sumatera-barat', 'Sumatera Barat'),
    ('sumatera-utara', 'Sumatera Utara'),
    ('dki-jakarta', 'DKI Jakarta'),
    ('jawa-tengah', 'Jawa Tengah'),
    ('kepulauan-riau', 'Kepulauan Riau'),
    ('banten', 'Banten'),
    ('di-yogyakarta', 'DI Yogyakarta'),
    ('bangka-belitung', 'Bangka Belitung'),
    ('jawa-barat', 'Jawa Barat'),
    ('bali', 'Bali'),
)


DAYS_OF_WEEK = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
)


class User(AbstractUser):

    role = models.CharField(max_length=15, choices=ROLE_CHOICE)
    app_access = models.ForeignKey('Apps', on_delete=models.SET_NULL, null=True, blank=True, related_name="apps")

    @property
    def is_developer(self):
        if getattr(self, 'role') == 'developer':
            return True
        return False

    @property
    def is_director(self):
        if getattr(self, 'role') == 'director':
            return True
        return False

    @property
    def is_secretary(self):
        if getattr(self, 'role') == 'secretary':
            return True
        return False

    @property
    def is_coordinator(self):
        if getattr(self, 'role') == 'coordinator':
            return True
        return False

    @property
    def is_pic(self):
        if getattr(self, 'role') == 'pic':
            return True
        return False

    # @property
    # def has_access_sppr(self):
    #     if hasattr(self, 'sppr')

    def __str__(self) -> str:
        return self.email


class Apps(models.Model):

    name = models.CharField(max_length=7, choices=APP_CHOICE)
    user = models.ManyToManyField('User')

    def __str__(self) -> str:
        return self.name
