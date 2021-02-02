from django.views.generic import ListView

from regions.models import Region
from .models import PharmacyMedicine


class MedicineList(ListView):
    paginate_by = 1
    template_name = "index.html"

    def get_queryset(self):
        return PharmacyMedicine.objects.select_related("medicine", "pharmacy").order_by("-price")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["regions"] = Region.objects.all().order_by("-id")
        return context
