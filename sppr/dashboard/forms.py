from django.db import models
from django.forms import ModelForm
from .models import Endorsement


class EndorsementForm(ModelForm):

    class Meta:
        model = Endorsement
        fields = '__all__'
