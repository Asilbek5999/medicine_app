import csv
import os
import random

from config.settings import BASE_DIR
from medicines.models import Medicine


def insert_medicines():
    fhand = open(
        os.path.join(BASE_DIR, "medicines/csv_data/medicine_list.csv"),
        encoding="utf8",
    )
    reader = csv.reader(fhand)
    header = next(reader)
    medicines_instances = []
    if header is not None:
        for row in reader:
            medicine = Medicine(barcode=row[0], title=row[1], manufacturer='', description='', medicine_type=random.choice(Medicine.MedicineType.values))
            medicines_instances.append(medicine)
        Medicine.objects.bulk_create(medicines_instances)
        print("Successfully added")

def run():
    insert_medicines()
