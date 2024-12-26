from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator , ValidationError  # Import `ValidationError`
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField() #<---- Chú ý phải dùng là `birth_day` 
    phone = models.CharField(max_length=20, blank=True, null=True, unique = True )  # <-- Thêm unique
    email = models.EmailField(blank=True, null=True, unique = True )  # <-- Thêm unique
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} ({self.pk})'


class Pet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    birth_day = models.DateField()
    gender = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
         return f'{self.name} ({self.pet_type} , {self.breed or "N/A"} ) - (Customer: {self.customer.name})'



class MedicalHistory(models.Model):

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medical_histories')
    appointment_time = models.DateTimeField(default=timezone.now, editable=True)
    symptoms = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    veterinarian = models.ForeignKey('Veterinarian', on_delete=models.SET_NULL, blank=True, null=True)
    prescriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2, default = 0,validators=[MinValueValidator(0.00)],  )
    def __str__(self):
        return f'History of {self.pet.name} ({self.pk}) - time {self.appointment_time}'

class Vaccine(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vaccines')
    vaccine_name = models.CharField(max_length=255)
    injection_date = models.DateField()
    re_injection_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f'Vaccine {self.vaccine_name} - (pet:{self.pet.name}) - {self.injection_date} '


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    veterinarian = models.ForeignKey('Veterinarian', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='appointments'
    )
    appointment_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
         ('completed', 'Completed')

    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_fee = models.DecimalField(max_digits=10, decimal_places=2, default = 0 ,validators=[MinValueValidator(0.00)]  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f'Appoint to pet {self.pet.name} - time {self.appointment_time} (id={self.pk},status = {self.status}  ) '


class Veterinarian(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    available_time = models.CharField(max_length=255, blank = True, null=True )
    phone = models.CharField(max_length=20, blank=True, null = True,  unique = True )  # <---- add
    email = models.EmailField(blank=True, null=True, unique = True)  # <---- add

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Dr.{self.name} ({self.specialty},id = {self.pk}) '

class CageRoom(models.Model):
     name = models.CharField(max_length=255)
     ROOM_TYPE_CHOICES = [
        ('admission', 'Admission Room'),
        ('treatment', 'Treatment Room')
     ]

     room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='admission')
     capacity = models.IntegerField(default=1 ,validators=[MinValueValidator(0)])
     STATUS_CHOICES = [
        ('vacant', 'Vacant'),
        ('occupied', 'Occupied'),
    ]
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='vacant')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     def __str__(self):
         return f'{self.name} ({self.room_type}, capacity = {self.capacity}  )'


class Review(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name = 'reviews')
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)] ,default = 0)
    comment = models.TextField(blank=True, null = True)
    review_date = models.DateTimeField(auto_now_add = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
         return f'{self.pk}:  Appoint - rating: {self.rating} ({self.comment}) '


class Admission(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,related_name = 'admissions')
    cage_room = models.ForeignKey(CageRoom, on_delete=models.SET_NULL, blank=True, null = True)
    admission_date = models.DateTimeField()
    estimated_discharge_date = models.DateTimeField(blank=True, null = True)
    notes = models.TextField(blank=True, null = True, max_length = 1024 )   # <-- added max length

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
          return f'Admission for Pet {self.pet.name}, Room  ({self.cage_room}), date:{self.admission_date}'



def validate_payment_time_not_before_appointment_time(payment_time_value, appointment_time):
  if payment_time_value and appointment_time:
        if payment_time_value < appointment_time:
               raise ValidationError(
                       "payment_time must not be less than the Appointment time.",
                   )


class Bill(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete = models.CASCADE, related_name='bill')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)],  )
    itemized_costs = models.TextField(blank = True, null=True )
    payment_time = models.DateTimeField(blank=True, null=True ,  )   # validators=[validate_payment_time_not_before_appointment_time ] # removed validation ( this will cause problem if data does not contain datetime field ( you have to default before )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return f'Invoice: {self.appointment.pk}  - {self.total_amount} - pay time:{self.payment_time} '

    def save(self, *args, **kwargs):  # added code
          # set validate when save for edit model
              # validation in save record
             if self.pk :
                #  # find data of current
                  validate_payment_time_not_before_appointment_time(self.payment_time,self.appointment.appointment_time   )
                 # call validation

                # original obj


             super().save(*args,**kwargs) # execute  when valid logic pass . otherwise validation errors.

class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
           return f'account {self.pk} user: {self.user}  '

   #   from django.db import models
class Configuration(models.Model):
     key = models.CharField(max_length = 255, unique = True) # unique value can create config name can use single key ( instead list name of array of value )
     value = models.TextField( )

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self): # it very helpfull for display value from this object . For example in other UI pages when debugging 
          return f'{self.key}:  - ({self.value}) ' # a quick value show of fields data from table db
     
class Statistic(models.Model):
    period = models.DateField()
    report_type = models.CharField(max_length = 255)
    value = models.DecimalField(max_digits=19,decimal_places=4,  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
         return f' report ({self.report_type}) time {self.period}  - result : {self.value}'