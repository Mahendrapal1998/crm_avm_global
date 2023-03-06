from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('login',views.login),
    path('admin',views.admin),
    path('leads',views.leads),
    path('addlead',views.addlead),
    path('leadview',views.leadview),
    path('editlead',views.editlead),
    path('saveeditlead',views.saveeditlead),
    path('savelead',views.savelead),
    path('clients',views.clients),
    path('institute',views.institute),
    path('addinstitute',views.addinstitute),
    path('courses',views.courses),
    path('addcourses',views.addcourses),
    path('user',views.user),
    path('adduser',views.adduser),
    path('task',views.task),
    path('addtask',views.addtask),
    path('products',views.products),
    path('addproduct',views.addproduct),
    path('newsletter',views.newsletter),
    path('accounts',views.accounts),
    path('meetings',views.meetings),
    path('quotes',views.quotes),
    path('invoices',views.invoices),
    path('upload',views.upload),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)