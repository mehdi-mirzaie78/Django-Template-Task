from django.shortcuts import render
from django.views import View
from .models import Passenger
from .forms import TitanicForm
from .utils import insert_data_from_dataset


class TitanicView(View):
    form_class = TitanicForm
    template_name = 'titanic.html'

    def get(self, request):
        passengers = Passenger.objects.all()
        return render(request, self.template_name, {"form": self.form_class, "passengers": passengers})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.cleaned_data['dataset']
            passengers = insert_data_from_dataset(dataset)
            return render(request, self.template_name, {"form": form, "passengers": passengers})
        return render(request, self.template_name, {"form": form})

