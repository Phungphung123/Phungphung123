from django.db import models

# Create your models here.

class Appointment(models.Model):
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='appointments')
    veterinarian = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_appointments')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')))
    fee_paid = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.pet.name} - {self.date}"
