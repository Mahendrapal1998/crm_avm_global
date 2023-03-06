from django.db import models

class FilesUpload(models.Model):
	file=models.FileField()
class Leads(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.IntegerField()
	title=models.CharField(max_length=200)
	visa_expiry=models.DateField()
	lead_owner=models.CharField(max_length=200,null=True,blank=True)
	visa_preference=models.CharField(max_length=200,null=True,blank=True)
	lead_source=models.CharField(max_length=200,null=True,blank=True)
	rating=models.CharField(max_length=200,null=True,blank=True)
	address=models.CharField(max_length=250,null=True,blank=True)
	city=models.CharField(max_length=200,null=True,blank=True)
	state=models.CharField(max_length=200,null=True,blank=True)
	post_code=models.IntegerField(null=True,blank=True)
	country=models.CharField(max_length=200,null=True,blank=True)
	enquiry_type=models.CharField(max_length=200,null=True,blank=True)
class Accounts(models.Model):
	account_owner=models.CharField(max_length=200)
	account_name=models.CharField(max_length=200)
	account_type=models.CharField(max_length=200)
	account_code=models.IntegerField()
	address=models.CharField(max_length=200)
class Tasks(models.Model):
	task_owner=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	due_date=models.DateField()
	account=models.CharField(max_length=200)
	status=models.CharField(max_length=200)
	priority=models.CharField(max_length=200)
class Meetings(models.Model):
	title=models.CharField(max_length=200)
	fromm=models.DateTimeField(auto_now_add=True)
	to=models.DateTimeField(auto_now_add=True)
	location=models.CharField(max_length=200)
class Products(models.Model):
	product_name=models.CharField(max_length=200)
	code=models.IntegerField()
	price=models.IntegerField()
class Quotes(models.Model):
	quote_owner=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	product_name=models.CharField(max_length=200)
	client_name=models.CharField(max_length=200)
	account_name=models.CharField(max_length=200)
	valid_until=models.DateField();
class Invoices(models.Model):
	invoice_owner=models.CharField(max_length=200)
	client_name=models.CharField(max_length=200)
	account_name=models.CharField(max_length=200)
	product_name=models.CharField(max_length=200)
	created_on=models.DateField();
	due_date=models.DateField();
