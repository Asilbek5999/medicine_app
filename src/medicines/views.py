from django.conf import settings
from django.views.generic import ListView

from .models import PharmacyMedicine


class MedicineList(ListView):
    paginate_by = 10
    template_name = "base.html"
    queryset = PharmacyMedicine.objects.all()

    def get_queryset(self):
        print("static root:",settings.STATIC_ROOT)
        print("base dir :", settings.BASE_DIR)
        return self.queryset