from django.shortcuts import render

# Create your views here.

def detail(request):
    name = "detail"
    return render(request, 'detail.html')