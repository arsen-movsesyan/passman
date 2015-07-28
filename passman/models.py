from django.db import models
from datetime import date,timedelta
from django.db.models import Max



# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = 'category'

    def __str__(self):
	return self.category_name




class Account(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    category =  models.ForeignKey('Category',related_name='belong_accounts')
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    acct_name = models.CharField(max_length=255,unique=True)
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
	return self.acct_name

    class Meta:
	managed = False
	db_table = 'acct'
	ordering = ['created_at']


class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=255,blank=False,unique=True)

    class Meta:
	managed = False
	db_table = 'attribute'

    def __str__(self):
	return self.attribute_name


class AccountAttributeModel(models.Model):
    id = models.AutoField(primary_key=True)
    acct = models.ForeignKey('Account',related_name='attributes')
    attr = models.ForeignKey('Attribute',related_name='attributes')
    acct_value = models.CharField(max_length=255)

    class Meta:
	managed = False
	db_table = 'account_attribute'



class Payment(models.Model):
    acct = models.OneToOneField('Account',related_name='payment_obj',db_column='acct_id',primary_key=True)
    due_date_day = models.IntegerField(blank=True)
    month_frequency = models.IntegerField(blank=True)
    auto_payment = models.BooleanField(default=False)

    class Meta:
	managed = False
	db_table = 'payment'

    def __str__(self):
	return self.acct.acct_name


    def get_due_date(self):

	due_date=date(date.today().year,date.today().month,self.due_date_day)
	last_payment=self.payment_history.aggregate(Max('payment_date'))['payment_date__max']

	if due_date < date.today():
	    due_date=date(date.today().year,date.today().month+self.month_frequency,self.due_date_day)

	ret={'due_date':due_date,'show_payment':True,'auto_payment':self.auto_payment}
	if not last_payment or date.today() - last_payment > timedelta(days=self.month_frequency*30):
	    return ret

	if due_date - timedelta(days=self.month_frequency*30) < last_payment:
	    due_date+=timedelta(days=self.month_frequency*30)
	    ret['show_payment']=False
	    ret['due_date']=due_date
	return ret


class PaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    acct = models.ForeignKey('Payment',related_name='payment_history',db_column='acct_id')
    payment_date = models.DateField()
    payment_amount = models.CharField(max_length=255)
    confirmation_code = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = 'payment_history'
	ordering = ['payment_date']

