from django.urls  import path 
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns=[
    path('index',index),
    path('detail-page',detailpage),
    path('about-page',about),
    path('faq-page',faq),
    path('contact-page',contact)

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)