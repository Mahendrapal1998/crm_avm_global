from django.urls import path,include

urlpatterns = [
    path('crmadmin/',include('crmadmin.urls')),
]
