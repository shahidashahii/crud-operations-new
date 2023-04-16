from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse
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
    LOW=Webpage.objects.all()

    LOW=Webpage.objects.filter(name__startswith='k')
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__contains='d')
    LOW=Webpage.objects.filter(name__in=('Dhoni','kohli'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='virat'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__gte='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__lte='2023-10-10')
    LOA=AccessRecord.objects.filter(date__lt='2022-03-10')
    LOA=AccessRecord.objects.filter(date__year='2023')
    LOA=AccessRecord.objects.filter(date__month='10')
    LOA=AccessRecord.objects.filter(date__day='10')
    LOA=AccessRecord.objects.filter(date__year__gt='2022')
    LOA=AccessRecord.objects.filter(date__month__lt='10')
    
    d={'access':LOA}
    return render(request,'display_access.html',d)

def update_webpage(request):
    Webpage.objects.filter(name='Kohli').update(email='Kohli@gmail.in')
    Webpage.objects.filter(name='pandya').update(topic_name='Chess')
    Webpage.objects.all()
    TO=Topic.objects.get_or_create(topic_name='Cricket')[0]
    TO.save()
    Webpage.objects.update_or_create(url='https://hardik.com',defaults={name='pandya','email':'hardik@gmail.com'})
    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpages.html',d)


