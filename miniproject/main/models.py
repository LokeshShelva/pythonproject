# from django.db import models
from djongo import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Axis(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    minRange = models.CharField(max_length=20)
    maxRange = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Axis Class"


class AxisForm(forms.ModelForm):
    class Meta:
        model = Axis
        fields = ('name', 'unit', 'minRange', 'maxRange')


class Data(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    value = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Plot(models.Model):
    GRAPH_TYPES = (
        ("B", "Bar Graph"),
        ("C", "Compound Bar Graph"),
        ("L", "Line Graph"),
    )
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=1, choices=GRAPH_TYPES, default="B")
    yAxis = models.EmbeddedField(
        model_container=Axis, model_form_class=AxisForm)
    xAxis = models.EmbeddedField(
        model_container=Axis, model_form_class=AxisForm)

    data = models.ArrayField(model_container=Data)

    objects = models.DjongoManager()
