from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='pets')
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=255)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name