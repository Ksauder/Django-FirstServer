from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def home(request):
    
    context = {
        "randString": get_random_string(length=14)
    }

    return render(request, 'rand/randindex.html', context)