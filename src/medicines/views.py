from django_filters.views import FilterView
from .filters import MedicineFilter
from .models import PharmacyMedicine

class MedicineList(FilterView):
    paginate_by = 100
    template_name = "index.html"
    filterset_class = MedicineFilter

    def get_queryset(self):
        return PharmacyMedicine.objects.select_related("medicine",
                                                       "pharmacy",
                                                       "pharmacy__district") \
            .order_by("-price")
