from django.shortcuts import render, HttpResponse
from .models import News
# Create your views here.
def Home(request):
    context = {
        "name":"Peter Parker"
    }
    return render(request, 'home.html', context)


#def News(request):
 #   return render(request, 'news.html')

def NewsP(request):
    obj=News.objects.get(id=1)
    context={
        "data":obj
    }
    return render(request, 'news.html', context)

def Contact(request):
    return render(request, 'contact.html')