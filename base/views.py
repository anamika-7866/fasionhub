from django.shortcuts import render
from .models import *

def index(request):
    mainframe = MainFrame.objects.all()
    return render(request,'index.html',{'mainframe': mainframe})


def detailpage(request):
    return render(request,'product-detail.html')

def contact(request):
    return render(request,'contact.html')


def faq(request):
    return render(request,'faq.html')



def about(request):
    return render(request,'about.html')