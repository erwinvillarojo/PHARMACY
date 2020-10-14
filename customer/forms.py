from django import forms
from .models import *

class CustomerForm(forms.ModelForm):

      class Meta:
         model = Customer
         fields = ('firstname','lastname')
         

class MedicineForm(forms.ModelForm):

	class Meta:
		model = Medicine 
		fields = ('common_brand','category', 'generic_name')
	