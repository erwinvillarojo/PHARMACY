
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'customer'
urlpatterns = [
    #path('api/data', views.get_data, name='api-data'),

    #TEST URL  
    path('registration', views.CustomerRegistrationView.as_view(), name="createcustomer_view"),
    path('registration_med', views.MedicineRegistrationView.as_view(), name="createmedicine_view"),
    path('index', views.LandingIndexView.as_view(), name="indexLanding_view"),
    path('dashboard', views.DashboardView.as_view(), name="dashboardview"),
  
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
