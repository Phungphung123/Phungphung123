from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('veterinarian', 'Veterinarian'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    # Thêm related_name để tránh xung đột
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Tên liên kết ngược cho trường groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Tên liên kết ngược cho trường user_permissions
        blank=True,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

