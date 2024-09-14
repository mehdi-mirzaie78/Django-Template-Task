from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import BadRequest
from django.views import View
from django.db import IntegrityError
from django.contrib import messages
from .models import Passenger
from .forms import TitanicForm, PassengerForm
from .utils import insert_data_from_dataset


class TitanicView(View):
    form_class = TitanicForm
    template_name = 'titanic.html'

    def setup(self, request, *args, **kwargs):
        self.passengers = Passenger.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class, "passengers": self.passengers})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.cleaned_data['dataset']
            try:
                inserted_passengers = insert_data_from_dataset(dataset)
            except IntegrityError as ie:
                messages.error(request, _(str(ie)), "danger")

            except BadRequest as br:
                messages.error(request, _(str(br)), "danger")

            else:
                messages.success(request, _("Data inserted successfully."), "success")
                return render(request, self.template_name, {"form": form, "passengers": inserted_passengers})

            finally:
                return render(request, self.template_name, {"form": form, "passengers": self.passengers})


class PassengerCreateView(View):
    form_class = PassengerForm
    template_name = 'passenger-create.html'

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Passenger created successfully."), "success")
            return redirect("home:titanic")

        messages.error(request, _("Something went wrong!"), "danger")
        return render(request, self.template_name, {"form": self.form_class})


class PassengerUpdateView(View):
    form_class = PassengerForm
    template_name = 'passenger-update.html'

    def setup(self, request, *args, **kwargs):
        pk = kwargs['pk']
        self.passenger = get_object_or_404(Passenger, pk=pk)
        return super().setup(request, *args, **kwargs)

    def get(self, request, pk):
        form = self.form_class(instance=self.passenger)
        return render(request, self.template_name, {"form": form, "passenger": self.passenger})

    def post(self, request, pk):
        form = self.form_class(instance=self.passenger, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Passenger updated successfully."), "success")
        return render(request, self.template_name, {"form": form, "passenger": self.passenger})


class PassengerDeleteView(View):
    def get(self, request, pk):
        queryset = Passenger.objects.filter(pk=pk)
        if queryset.exists():
            passenger = queryset.get()
            queryset.delete()
            messages.success(request, f"Passenger: #{passenger.id} deleted successfully.", "success")
        return redirect("home:titanic")


class PassengerDeleteAllView(View):
    def get(self, request):
        queryset = Passenger.objects.all()
        queryset.delete()
        messages.success(request, "All data deleted successfully.", "success")
        return redirect("home:titanic")

