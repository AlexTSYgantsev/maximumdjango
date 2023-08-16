from django.shortcuts import render
from .models import Advertisements

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements':advertisements} # записали все объявления из advertisemnets в контекст(удобный формат для django)
    return render(request,'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
# Create your views here.
