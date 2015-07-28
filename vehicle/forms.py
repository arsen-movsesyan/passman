from django import forms
from django.forms import ModelForm

from vehicle.models import Vehicle,VehicleRegistration

# Create your tests here.


class AddVehicle(ModelForm):
    class Meta:
	model = Vehicle
	fields = ['v_make','v_model','v_year','vin','license_plate','purchase_date']



class EditVehicle(ModelForm):
    class Meta:
	model = Vehicle
	fields = ['nonoperational_date','retired']


class RenewVehicle(ModelForm):
    class Meta:
	model = VehicleRegistration
	fields = ['registration_issue_date','registration_expiration']


class RenewVehicleFromMenu(ModelForm):
    class Meta:
	model = VehicleRegistration
	fields = ['vehicle','registration_issue_date','registration_expiration']

