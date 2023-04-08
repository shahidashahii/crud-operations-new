from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lte='2023-10-10')
    d={'access':LOA}
    return render(request,'display_access.html',d)




