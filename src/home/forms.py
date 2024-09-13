from django import forms


class TitanicForm(forms.Form):
    dataset = forms.FileField()
