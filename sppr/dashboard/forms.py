from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Endorsement, Longlist


class EndorsementForm(ModelForm):

    class Meta:
        model = Endorsement
        fields = '__all__'


class LonglistForm(ModelForm):

    class Meta:
        model = Longlist
        fields = '__all__'
