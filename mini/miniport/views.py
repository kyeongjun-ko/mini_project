from django.shortcuts import render

# Create your views here.

def detail(request):
    #return HttpResponse("<h1>Hello World</h1>")
    #number = 10
    name = "kj"
    return render(request, 'detail.html')