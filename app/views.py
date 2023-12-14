from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def display_ar(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_ar.html',d)