from django.views.generic import ListView

from .models import PharmacyMedicine


class MedicineList(ListView):
    paginate_by = 1
    template_name = "index.html"

    def get_queryset(self):
        return PharmacyMedicine.objects.select_related("medicine", "pharmacy")