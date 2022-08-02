from django.contrib import admin
from .models import Departments,Doctors,Booking,Contact

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','sub','email','message')
admin.site.register(Contact,ContactAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','doc_name','booking_date','booked_on')
admin.site.register(Booking, BookingAdmin)