from django.db import models

# Create your models here.

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    v_make = models.CharField(max_length=255)
    v_model = models.CharField(max_length=255)
    v_year = models.CharField(max_length=4)
    vin = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=255)
    purchase_date = models.DateField()
    nonoperational_date = models.DateField(blank=True)
    retired = models.DateField(blank=True)

    class Meta:
	managed = False
	db_table = 'vehicle'


    def __str__(self):
	return "{0} {1}".format(self.v_make,self.v_model)


class VehicleRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicle',related_name='registrations')
    registration_issue_date = models.DateField()
    registration_expiration = models.DateField()

    class Meta:
	managed = False
	db_table = 'vehicle_registration'



class VehicleRegistrationView(models.Model):
    id = models.IntegerField(primary_key=True)
    v_make = models.CharField(max_length=255)
    v_model = models.CharField(max_length=255)
    v_year = models.CharField(max_length=4)
    license_plate = models.CharField(max_length=255)
    vin = models.CharField(max_length=255)
    last_issue_date = models.DateField()
    expiration_date = models.DateField()
    time_left = models.IntegerField()

    class Meta:
	managed = False
	db_table = 'vehicle_registration_view'
