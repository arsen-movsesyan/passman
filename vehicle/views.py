from django.shortcuts import render

from datetime import timedelta,date

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import Vehicle,VehicleRegistrationView,VehicleRegistration
from .forms import AddVehicle,EditVehicle,RenewVehicleFromMenu,RenewVehicle
# Create your views here.


def see_all_vehicles(request):
    cars=Vehicle.objects.all()
    template=loader.get_template('vehicle/all_vehicles.html')
    context=RequestContext(request,{'cars':cars})
    return HttpResponse(template.render(context))


def issue_date_lookup(request):
    cars=VehicleRegistrationView.objects.all()
    template=loader.get_template('vehicle/vehicle.html')
    context=RequestContext(request,{'cars':cars})
    return HttpResponse(template.render(context))



def add_vehicle(request):
    if request.method == 'POST':
	in_form=AddVehicle(request.POST)
	if in_form.is_valid():
	    new_car=in_form.save()
	    return HttpResponseRedirect('/all_vehicles')
	else:
	    template=loader.get_template('vehicle/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	out_form=AddVehicle()
	return render(request,'vehicle/add_vehicle.html',{'form':out_form})


def vehicle_edit(request,in_vehicle_id):
    vehicle_object=Vehicle.objects.get(pk=in_vehicle_id)
    if request.method == 'POST':
	in_form=EditVehicle(request.POST,instance=vehicle_object)
	if in_form.is_valid():
	    in_form.save()
	    return HttpResponseRedirect('/vehicle')
	else:
	    template=loader.get_template('vehicle/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	out_form=EditVehicle(instance=vehicle_object)
	context={'form':out_form,'vehicle_id':in_vehicle_id}
	return render(request,'vehicle/edit_vehicle.html',context)




def renew_from_menu(request):
    if request.method == 'POST':
	in_form=RenewVehicleFromMenu(request.POST)
	if in_form.is_valid():
	    in_form.save()
	    return HttpResponseRedirect('/vehicle')
	else:
	    template=loader.get_template('vehicle/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	out_form=RenewVehicleFromMenu()
	context={'form':out_form}
#	return render(request,'vehicle/renew_from_menu.html',context)
	return render(request,'vehicle/edit_vehicle.html',context)


def vehicle_renew(request,in_vehicle_id):
    vehicle_object=Vehicle.objects.get(pk=in_vehicle_id)
    if request.method == 'POST':
	in_form=RenewVehicle(request.POST,instance=vehicle_object)
	if in_form.is_valid():
	    vehicle_registration=VehicleRegistration.objects.create(
		    vehicle=vehicle_object,
		    registration_issue_date=in_form.cleaned_data['registration_issue_date'],
		    registration_expiration=in_form.cleaned_data['registration_expiration']
	    )
#	    in_form.save()
	    return HttpResponseRedirect('/vehicle')
	else:
	    template=loader.get_template('vehicle/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	out_form=RenewVehicle(instance=vehicle_object)
	context={'form':out_form,'vehicle':vehicle_object}
	return render(request,'vehicle/renew_vehicle.html',context)

