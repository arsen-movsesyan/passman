from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from datetime import date



from passman.models import Account,Attribute,Category,Payment,PaymentHistory

# Create your tests here.


#class OnClickChoiceField(forms.ModelChoiceField):
#    class Meta:
#	js = ('onclick.js')


class AddCategoryForm(ModelForm):
    class Meta:
	model = Category
	fields = ['category_name','description']


class AddAccountForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select Category',label='Category',
	widget=forms.Select(attrs={'onfocus':"this.oldvalue = this.value;",
	'onchange':"onChangeTest(this);this.oldvalue = this.value;"}))
    class Meta:
	model = Account
	fields = ['acct_name','category','login','passwd','url','description']


class EditAccountForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select Category',label='Category',
	widget=forms.Select(attrs={'onfocus':"this.oldvalue = this.value;",
	'onchange':"onChangeTest(this);this.oldvalue = this.value;"}))
    class Meta:
	model = Account
	fields = ['active','passwd','url','category','description']


class AddAttributesForm(forms.Form):
    attr_name = forms.ModelChoiceField(queryset=Attribute.objects.all(),empty_label='Select Attribute',label='Attribute')
    attr_value = forms.CharField(label='Value')


class AddAttributeForm(ModelForm):
    class Meta:
	model = Attribute
	fields = ['attribute_name']


class AcctSearch(forms.Form):
    search_field=forms.CharField(label='Search')


class PaymentForm(ModelForm):
    due_date_day = forms.IntegerField(label='Due Day')
    month_frequency = forms.IntegerField(label='Month')
    class Meta:
	model = Payment
	fields = ['due_date_day','month_frequency','auto_payment']


class PaymentHistoryForm(ModelForm):
    payment_date = forms.DateField(widget=SelectDateWidget,initial=date.today())
    class Meta:
	model = PaymentHistory
	fields = ['payment_date','payment_amount','confirmation_code']
