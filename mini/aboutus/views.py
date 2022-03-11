from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    #number = 10
    name = "michael"
    return render(request, 'index.html')
