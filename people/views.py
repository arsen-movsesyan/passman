from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader




from .models import Person,AddressHistory

# Create your views here.
def person(request):
    people=Person.objects.all()
    template=loader.get_template('people/people.html')
    context=RequestContext(request,{'ssn':people})
    return HttpResponse(template.render(context))


def address_history(request):
    addrs=AddressHistory.objects.all()
    template=loader.get_template('people/address.html')
    context=RequestContext(request,{'addrs':addrs})
    return HttpResponse(template.render(context))