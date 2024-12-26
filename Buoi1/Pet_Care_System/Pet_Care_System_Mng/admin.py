from django.contrib import admin
from .models import Configuration, Customer, Pet, MedicalHistory, Vaccine, Account, Admission, Appointment, Veterinarian, Review, Bill, Statistic, CageRoom


@admin.register(Customer) # this register to table admin with model customer 
class CustomerAdmin(admin.ModelAdmin): # Custom layout for display in table Admin Django
    list_display = ("name", "gender", "birth_day", "phone","email","id",) # Show attributes in listview of table on admin site
    list_filter = ("gender",)
    search_fields = ("name", "phone", "email") # Allow to search by this filed 

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "customer", "pet_type","breed", "birth_day", "gender", "id" ) # List columns of model Pet 
    list_filter = ("pet_type", "gender","customer")
    search_fields = ("name", "breed")


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ("pet", "appointment_time", "veterinarian", "diagnosis", "service_fee", "id" ) # fields shown in medical history record on Django admin view page
    list_filter = ("appointment_time", "veterinarian")  # Enable the record can be filter on field `appointment_time` , and field `veterinarian` on Django admin view
    search_fields = ("pet__name","diagnosis","symptoms")   # add field can filter records on view admin django
   # to define lookup relations you should using `__` , not dot, to refer relationship fields : pet.name will cause lookup issue

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ("pet", "vaccine_name", "injection_date", "re_injection_date", "id") #show vaccine field when querying list data at Admin UI.
    list_filter = ("injection_date", ) #allow data on date column on admin
    search_fields = ("vaccine_name", ) # allows for text search box 

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("pet", "veterinarian", "appointment_time", "status", "booking_fee","id" ) # set up data output of appointment records
    list_filter = ("status", "appointment_time")  # setup filer for records on booking time
    search_fields = ("pet__name", "status", ) # allow searching via pet name 

@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "available_time","id" )  # setup which fields on vet table will show up when calling get records on Admin UI.
    search_fields = ("name","specialty")  # let the admin can text search for vet name / vet's specicalty on admin UI page 

@admin.register(CageRoom)
class CageRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "room_type", "capacity", "status","id") # specify display fields at listview django
    list_filter = ("room_type","status")  # define field on table cage on django to can use the filters , help admin easy to filter record data in view of django admin ui
    search_fields = ("name", )  # define where can do searching record via name filed of this cage model class

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("appointment", "rating", "comment", "review_date", "id")   # admin django : record output for the reviews table list data output
    list_filter = ("rating",)    # help data can be filterd easily on review rating via UI in django Admin UI 
    search_fields = ("comment",)   # allow text search on comment when on Django admin panel .


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("pet", "cage_room", "admission_date","estimated_discharge_date","id") # Show detail record on table admission at Django admin view table list output
    list_filter = ("admission_date","estimated_discharge_date"  ) # setting what data allow user filter when on  list admission data output
    search_fields = ("pet__name",)  # make sure Admin panel able search using text via pet's name filed in data query.


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ("appointment", "total_amount","payment_time", "id") # define record list show when query output  
    search_fields = ("appointment__pet__name",)  # Make record able text search by appointment table  relation with name of Pet filed


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user","id", )# List of field will display when list this object record

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("key", "value","id")#list field when record on configuration table is output to view via Django admin UI page .
    search_fields=("key",) # Make configuration  table is text search via its key (name config name for easy query filter via Admin UI.)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
   list_display=("period","report_type","value", "id") # Output table Statistic records via these fields on Admin page. 
   search_fields=("report_type",) # can make record statistics able to search with this text in that fields report_type
   list_filter=("period",)  # can filter record using period for report statistic results.