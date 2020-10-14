from django.http import Http404
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CustomerForm
from .forms import MedicineForm
from .models import *

# Create your views here.

class LandingIndexView(View):
    
    def get(self, request):
        return render(request,'landing/index.html')
    def post(self, request):
        return render(request,'customer/customerReg.html')




class DashboardView(View):
    def get(self, request):
        qs_customer = Customer.objects.all()
        qs_medicines = Medicine.objects.all()

        contexts = { 

                'customers' : qs_customer,
                'medicines' : qs_medicines
        }    

        return render(request, 'dashboard/dashboard.html', contexts)

    def post(self, request):
        if request.method == 'POST':    
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                cid = request.POST.get("customer-id")            
                fname = request.POST.get("customer-firstname")
                mname = request.POST.get("customer-middlename")
                lname = request.POST.get("customer-lastname")
                a = request.POST.get("customer-address")
                birthdate = request.POST.get("customer-bdate")
                g = request.POST.get("customer-gender")
                s = request.POST.get("customer-status")
                sname = request.POST.get("customer-spouse_name")
                soccupation = request.POST.get("customer-spouse_occupation")
                nos_child = request.POST.get("customer-no_children")
                maname = request.POST.get("customer-mothers_name")
                mo = request.POST.get("customer-mothers_occupation")
                faname = request.POST.get("customer-fathers_name")
                fo = request.POST.get("customer-fathers_occupation")
                h = request.POST.get("customer-height")
                w = request.POST.get("customer-weight")
                religion = request.POST.get("customer-religion")
                p = request.FILES.get('profile_pic')
        
                update_student = Customer.objects.filter(person_ptr_id = cid).update(firstname = fname, middlename = mname, lastname = lname, address = a, bdate = birthdate, gender = g, status = s, spouse_name = sname,
                                                         spouse_occupation = soccupation, no_children = nos_child, mothers_name = maname, mothers_occupation = mo, fathers_name = faname, fathers_occupation = fo, height = h, weight = w, religion = religion, profile_pic = p)
                print(update_student)
                print('profile updated')

            elif'btnDelete' in request.POST:   
                print('delete button clicked')
                cid = request.POST.get("customer-id")
                cus = Customer.objects.filter(person_ptr_id=cid).delete()
                pers = Person.objects.filter(id = cid).delete()
                print('recorded deleted')
            #return redirect('customer:dashboardview')

            if 'btnUpdate' in request.POST:
                print('update medicine button clicked')
                mid = request.POST.get("medicine-id")    
                sku = request.POST.get("medicine-sku")
             
                category = request.POST.get("medicine-category")
                generic = request.POST.get("medicine-generic")
                common = request.POST.get("medicine-common")
                mdate = request.POST.get("medicine-manufactured")
                edate = request.POST.get("medicine-expiry")
                s = request.POST.get("medicine-size")
                p = request.POST.get("medicine-price")
                i = request.POST.get("medicine-items")
                se = request.POST.get("medicine-effects")
                use = request.POST.get("medicine-use")
                new_image1 = request.FILES.get('medicine-img1', None)
                new_image2 = request.FILES.get('medicine-img2', None)
                new_image3 = request.FILES.get('medicine-img3', None)
                update_medicine = Medicine.objects.filter(id = mid).update(sku = sku, category = category, generic_name = generic, common_brand = common, manufactured_date = mdate, expiry_date = edate,
                                            size = s, price = p, no_of_items = i, side_effects = se, how_to_use = use, img1 = new_image1, img2 = new_image2, img3 = new_image3 )
 
                print(update_medicine)
        
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                mid = request.POST.get('medicine-id')
                med = Medicine.objects.filter(id = mid).delete()
                print('medicine deleted')
                
                
            elif 'btnOrder' in request.POST:
                
               
                mid = request.POST.get("medicine-id")  
                medItems = request.POST.get("medicine-items")
                order = request.POST.get("order")
                price = request.POST.get("medicine-totalPrice")
                total = (float(order) * float(price))
              
                total= request.POST.get("total")
                   
                i = (int(medItems)-int(order))
             
                
                                                                          
                update_m = Medicine.objects.filter(id = mid).update(no_of_items = i, order = order) 
                #update_s = CustomerAcquiresMedicine.objects.filter(id = cid).update( order = order) 
            
                print(update_m)
               
                print('Medicine Updated')
   
        return redirect('customer:dashboardview')
       

class CustomerRegistrationView(View):
    
    def get(self, request):
        return render(request,'customer/customerReg.html')

    def post(self, request):       
        form = CustomerForm(request.POST)

        if form.is_valid():
            #try
            fname = request.POST.get("firstname")
            mname = request.POST.get("middlename")
            lname = request.POST.get("lastname")
            a = request.POST.get("address")
            birthdate = request.POST.get("bdate")
            g = request.POST.get("gender")
            s = request.POST.get("status")
            sname = request.POST.get("spouse_name")
            soccupation = request.POST.get("spouse_occupation")
            nos_child = request.POST.get("no_children")
            maname = request.POST.get("mothers_name")
            mo = request.POST.get("mothers_occupation")
            faname = request.POST.get("fathers_name")
            fo = request.POST.get("fathers_occupation")
            h = request.POST.get("height")
            w = request.POST.get("weight")
            religion = request.POST.get("religion")
            #p = request.FILES['profile_pic']
            p = request.FILES.get('profile_pic')
            form = Customer(firstname = fname, middlename = mname, lastname = lname, address = a, bdate = birthdate, gender = g, date_registered = timezone.now(), status = s, spouse_name = sname,
                            spouse_occupation = soccupation, no_children = nos_child, mothers_name = maname, mothers_occupation = mo, fathers_name = faname, fathers_occupation = fo, height = h, weight = w, religion = religion, profile_pic = p)

            form.save()

            return redirect('customer:dashboardview')
          
            # except:
            #   raise Http404
            
        else:
            print(form.errors)
            return HttpResponse('not valid')



class MedicineRegistrationView(View):
    def get(self, request):
        return render(request, 'medicine/medicineReg.html')

    def post(self, request):
        form = MedicineForm(request.POST)
        if form.is_valid():

             dregistered = request.POST.get("date_registered")
             stock_unit = request.POST.get("sku")
             order = request.POST.get("order")
             category = request.POST.get("category")
             generic = request.POST.get("generic_name")
             common = request.POST.get("common_brand")
          
             size = request.POST.get("size")
             price = request.POST.get("price")
             items = request.POST.get("no_of_items")
             mdate = request.POST.get("manufactured_date")
             edate = request.POST.get("expiry_date")
             se = request.POST.get("side_effects")
             use = request.POST.get("how_to_use")
             image1 = request.FILES.get('img1')
             image2 = request.FILES.get('img2')
             image3 = request.FILES.get('img3')

            
             form = Medicine(date_registered = dregistered, sku = stock_unit, category = category, generic_name = generic, common_brand= common, 
                             manufactured_date = mdate, expiry_date = edate, size = size, price = price, no_of_items = items, side_effects = se, 
                             how_to_use = use, img1 = image1, img2 = image2, img3 = image3, order =order)

             form.save()
            
             return redirect('customer:dashboardview')
          
             # return render(request,'index.html')
             # except:
             #   raise Http404
        else:
             print(form.errors)
             return HttpResponse('not valid')




