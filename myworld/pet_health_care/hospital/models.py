from django.db import models

# Create your models here.
from django.db import models

class HospitalStay(models.Model):
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return f"{self.pet.name} - {self.check_in_date}"
