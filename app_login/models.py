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

MENU_CHOICE = (
    ('kajian-kewilayahan', 'Kajian Kewilayahan'),
    ('situs-rajawali', 'Situs Rajawali'),
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

    # pic_provinsi = models.CharField(choices=PIC_CHOICE, max_length=50)
    role = models.ForeignKey('Role', verbose_name="Role", related_name="Role", on_delete=models.SET_NULL, null=True)
    login_status = models.BooleanField(default=False, editable=False)

    @property
    def get_user_login_status(self):
        return self.login_status

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

    # def save( self, force_insert: bool = ..., force_update: bool = ...,
    #           using: Optional[str] = ..., update_fields: Optional[Iterable[str]] = ...) -> None:
    #     return super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return '%s | %s' % (self.email, self.username)


class Role(models.Model):

    name = models.CharField(max_length=15, choices=ROLE_CHOICE)
    app_access = models.ManyToManyField("App", verbose_name='App(s) Access', related_name='AppAccess')


class App(models.Model):

    name = models.CharField(max_length=7, choices=APP_CHOICE)
    list_menu = models.ManyToManyField('Menu', related_name='Menu')

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):

    name = models.CharField(choices=MENU_CHOICE, max_length=30)

    def __str__(self) -> str:
        return self.name
