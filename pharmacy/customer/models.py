from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length = 100)
    middlename = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    address = models.CharField(max_length = 50)
    bdate = models.DateField()
    gender = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "Person"


class Customer(Person):
    date_registered = models.DateField(default = timezone.now)
    status = models.CharField(max_length = 100)
    spouse_name = models.CharField(max_length = 100)
    spouse_occupation = models.CharField(max_length = 100)
    no_children = models.IntegerField()
    mothers_name = models.CharField(max_length = 100)
    mothers_occupation = models.CharField(max_length = 100)
    fathers_name = models.CharField(max_length = 100)
    fathers_occupation = models.CharField(max_length = 100)
    height = models.FloatField()
    weight = models.FloatField()
    religion = models.CharField(max_length = 100)
    profile_pic = models.FileField(upload_to='media', null = True)

    class Meta:
        db_table = "Customer"


class Medicine(models.Model):
    date_registered = models.DateField(auto_now_add = True)
    sku = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    generic_name = models.CharField(max_length = 100)
    common_brand = models.CharField(max_length = 100)
    size = models.IntegerField()
    price = models.FloatField()
    order = models.IntegerField()
    total = models.FloatField()
    no_of_items = models.IntegerField()
    manufactured_date = models.DateField()
    expiry_date = models.DateField()
    side_effects = models.TextField(max_length = 200)    
    how_to_use = models.TextField(max_length = 200)
    img1 = models.FileField(upload_to='media', null = True)
    img2 = models.FileField(upload_to='media', null = True)
    img3 = models.FileField(upload_to='media', null = True)

    
    class Meta:
        db_table = "Medicine"


class CustomerAcquiresMedicine(models.Model):
    customer = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE, related_name = "Customer")
    medicine = models.ForeignKey(Medicine, null = False, blank = False, on_delete = models.CASCADE, related_name = "Medicine")
    order = models.IntegerField( blank = False,)
 

    class Meta:             
        db_table = "CustomerAcquired"









