from django.urls import path

from .views import MedicineList

app_name = "medicines"

urlpatterns = [
    path("", MedicineList.as_view(), name="list"),

]
