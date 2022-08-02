
from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=250)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    name = models.CharField(max_length=250)
    spec = models.CharField(max_length=250)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.name + '- ('+self.spec + ')'

class Booking(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=250)
    sub = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name