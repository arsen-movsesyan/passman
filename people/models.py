from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    dob = models.DateField()
    ssn_13 = models.CharField(max_length=3)
    ssn_45 = models.CharField(max_length=3)
    ssn_69 = models.CharField(max_length=3)

    class Meta:
	managed = False
	db_table = 'ssn'


class AddressHistory(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    str_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    comments = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = 'address_history'
	ordering = ['start_date']
