from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.db.models import Max


from .models import Account,Attribute,AccountAttributeModel,Category,Payment,PaymentHistory
from .forms import AcctSearch,AddAccountForm,AddAttributeForm,EditAccountForm,AddAttributesForm,AddCategoryForm
from .forms import PaymentHistoryForm,PaymentForm
from datetime import date,timedelta
from django.conf import settings

# Create your views here.




def accounts(request,in_acct_iden):
    template='passman/all_accounts.html'
    if request.method == 'POST':
	search_form=AcctSearch(request.POST)
	if search_form.is_valid():
	    accounts=Account.objects.filter(acct_name__icontains=search_form.cleaned_data['search_field'])
	else:
	    accounts=Account.objects.filter(active=True)
    else:
	if in_acct_iden == 'all':
	    accounts=Account.objects.all()
	else:
	    accounts=Account.objects.filter(active=True)
    return list_accounts(request,template,accounts)


def payments(request):
    template='passman/payment_accounts.html'
    if request.method == 'POST':
	search_form=AcctSearch(request.POST)
	if search_form.is_valid():
	    accounts=Account.objects.filter(acct_name__icontains=search_form.cleaned_data['search_field'])
	else:
	    accounts=Account.objects.filter(active=True)
	return list_accounts(request,template,accounts)
    else:
	search_form=AcctSearch()
	template=loader.get_template(template)
	accounts=Account.objects.filter(active=True).filter(category=2)
	array=[]
	for acct in accounts:
	    info={}
	    info['obj']=acct

	    d_d_d=acct.payment_obj.get_due_date()
	    due_date=d_d_d['due_date']
	    days_left = (due_date - date.today()).days

	    show_payment=d_d_d['show_payment']
	    color='red'
	    if days_left > settings.WARNING_VALUE:
		color='#00ff00'
	    elif days_left > settings.CRITICAL_VALUE:
		color='yellow'
	    info['color']=color
	    info['due_date']=due_date
	    info['days_left']=days_left
	    info['show_payment']=show_payment
	    info['auto_payment']=d_d_d['auto_payment']
#	    if d_d_d['auto_payment']:
#		info['show_payment']=False
	    array.append(info)
	context=RequestContext(request,{'accts':array,'search_form':search_form})
	return HttpResponse(template.render(context))


def list_accounts(request,in_template,in_accounts):
    search_form=AcctSearch()
    template=loader.get_template(in_template)
    context=RequestContext(request,{'accts':in_accounts,'search_form':search_form})
    return HttpResponse(template.render(context))


def add_account(request):
    if request.method == 'POST':
	in_form=AddAccountForm(request.POST)
	if in_form.is_valid():
	    category=in_form.cleaned_data['category']
	    if category.id == 2:
		ext_form=ext_form=PaymentForm(request.POST)
		if ext_form.is_valid():
		    new_account=in_form.save()
		    payment_object=Payment.objects.create(
			    acct=new_account,
			    due_date_day=ext_form.cleaned_data['due_date_day'],
			    month_frequency=ext_form.cleaned_data['month_frequency'],
			    auto_payment=ext_form.cleaned_data['auto_payment'])
		    urlToRedirect="/acct/{0}".format(new_account.id)
		    return HttpResponseRedirect(urlToRedirect)
		else:
		    template=loader.get_template('passman/err_template.html')
		    return HttpResponse(template.render({'form':ext_form}))
	    else:
		new_account=in_form.save()
		urlToRedirect="/acct/{0}".format(new_account.id)
		return HttpResponseRedirect(urlToRedirect)
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	template = 'passman/edit_account.html'
	out_form = AddAccountForm()
	ext_form = PaymentForm()
	return render(request,template,{'form':out_form,'ext_form':ext_form,'action_type':'add'})



def single_account(request,in_acct_id):
    account=Account.objects.get(pk=in_acct_id)
    aas=account.attributes.all()
    template=loader.get_template('passman/single_account.html')
    context=RequestContext(request,{'account':account,'aas':aas})
    return HttpResponse(template.render(context))



def manage_categories(request):
    if request.method == 'POST':
	in_form=AddCategoryForm(request.POST)
	if in_form.is_valid():
	    new_category=in_form.save()
	    return HttpResponseRedirect('manage_categories')
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	template='passman/manage_categories.html'
	categories=Category.objects.all()
	in_form=AddCategoryForm()
	context={'categories':categories,'form':in_form}
	return render(request,template,context)


def manage_attributes(request):
    if request.method == 'POST':
	in_form=AddAttributeForm(request.POST)
	if in_form.is_valid():
	    new_attribute=in_form.save()
	    return HttpResponseRedirect('manage_attributes')
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	template='passman/manage_attributes.html'
	attributes=Attribute.objects.all()
	in_form=AddAttributeForm()
	context={'attributes':attributes,'form':in_form}
	return render(request,template,context)


def edit_account(request,in_acct_id):
    account_object=Account.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form=EditAccountForm(request.POST,instance=account_object)
	if in_form.is_valid():
	    category=in_form.cleaned_data['category']
	    if category.id == 2:
		ext_form=ext_form=PaymentForm(request.POST)
		if ext_form.is_valid():
		    in_form.save()
		    p_o=Payment.objects.get(pk=in_acct_id)
		    if not p_o:
			payment_object=Payment.objects.create(
			    acct=account_object,
			    due_date_day=ext_form.cleaned_data['due_date_day'],
			    month_frequency=ext_form.cleaned_data['month_frequency'],
			    auto_payment=ext_form.cleaned_data['auto_payment'])
		    else:
			p_o.due_date_day=ext_form.cleaned_data['due_date_day']
			p_o.month_frequency=ext_form.cleaned_data['month_frequency']
			p_o.auto_payment=ext_form.cleaned_data['auto_payment']
			p_o.save()
		    urlToRedirect="/acct/{0}".format(in_acct_id)
		    return HttpResponseRedirect(urlToRedirect)
		else:
		    template=loader.get_template('passman/err_template.html')
		    return HttpResponse(template.render({'form':ext_form}))
	    else:
		in_form.save()
		urlToRedirect="/acct/{0}".format(in_acct_id)
		return HttpResponseRedirect(urlToRedirect)
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	template='passman/edit_account.html'
	in_form=EditAccountForm(instance=account_object)
	try:
	    ext_form = PaymentForm(instance=account_object.payment_obj)
	except Exception:
	    ext_form = PaymentForm()
	    pass
	context={'form':in_form,'account':account_object,'ext_form':ext_form,'action_type':'edit'}
	return render(request,template,context)


def add_edit_account_attributes(request,in_acct_id):
    acct_obj=Account.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form=AddAttributesForm(request.POST)
	if in_form.is_valid():
	    new_attribute=AccountAttributeModel.objects.create(
		acct_id=in_acct_id,
		attr_id=in_form.cleaned_data['attr_name'].id,
		acct_value=in_form.cleaned_data['attr_value'])
	    return HttpResponseRedirect("/acct/acct_attributes/{0}".format(in_acct_id))
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form=AddAttributesForm()
	template='passman/add_edit_attributes.html'
	aas=acct_obj.attributes.all()
	context={'account':acct_obj,'form':in_form,'aas':aas}
	return render(request,template,context)


def remove_acct_attribute(request,in_acct_id,in_attr_id):
    acct_attr=AccountAttributeModel.objects.filter(pk=in_attr_id)
    acct_attr.delete()
    return HttpResponseRedirect("/acct/acct_attributes/".format(in_acct_id))




def remove_attribute(request,in_attr_id):
    attribute=Attribute.objects.get(pk=in_attr_id)
    refs=attribute.attributes.all()
    if len(refs) > 0:
	accts=[]
	for aa in refs:
	    accts.append(aa.acct)
	return render(request,'passman/cannot_remove_attr.html',{'object':'attribute','attr':attribute,'accts':accts})
    else:
	attribute.delete()
	return HttpResponseRedirect('/acct/manage_attributes')


def remove_category(request,in_cat_id):
    category=Category.objects.get(pk=in_cat_id)
    refs=category.belong_accounts.all()
    if len(refs) > 0:
	return render(request,'passman/cannot_remove_attr.html',{'object':'category','attr':category,'accts':refs})
    else:
	category.delete()
	return HttpResponseRedirect('/acct/manage_categories')


def acknowledge(request,in_acct_id):
    payment_obj=Payment.objects.get(pk=in_acct_id)
    acct_obj=Account.objects.get(pk=in_acct_id)
    if request.method == 'POST':
	in_form = PaymentHistoryForm(request.POST)
	if in_form.is_valid():
#	    payment=Payment.objects.get(pk=in_acct_id)
	    p_h=PaymentHistory.objects.create(
		acct=Payment.objects.get(pk=in_acct_id),
		payment_date=in_form.cleaned_data['payment_date'],
		payment_amount=in_form.cleaned_data['payment_amount'],
		confirmation_code=in_form.cleaned_data['confirmation_code'])
	    return HttpResponseRedirect('/acct/payments')
	else:
	    template=loader.get_template('passman/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form = PaymentHistoryForm()
	template='passman/acknowledge_payment.html'
	context={'account':acct_obj,'form':in_form}
	return render(request,template,context)


def payment_history(request,in_acct_id):
    payment_obj=Payment.objects.get(pk=in_acct_id)
    p_h=payment_obj.payment_history.all()
    print p_h
    template=loader.get_template('passman/payment_history.html')
    context=RequestContext(request,{'account':payment_obj,'p_h':p_h})
    return HttpResponse(template.render(context))
    