from django import forms
from .models import Passenger


class TitanicForm(forms.Form):
    dataset = forms.FileField()


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = "__all__"
        exclude = ("id",)
