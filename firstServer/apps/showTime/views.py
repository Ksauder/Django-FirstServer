from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def home(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    return render(request, 'showTime/home.html', context)