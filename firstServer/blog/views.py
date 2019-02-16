from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return HttpResponse('<h1>Placeholder to later display a list of all blogs on the site. </h1>')

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    return redirect('/')

def show(request, number):
    context={
        'number': number
    }
    return render(request, 'blog/show.html', context)
