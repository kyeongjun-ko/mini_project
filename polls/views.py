from django.shortcuts import render, get_object_or_404
from polls.models import StoresDb

def index(request):
    return render(request, 'polls/index.html')


def detail_sunhan(request, x):
    store = get_object_or_404(StoresDb, idx=x)
    context = {'store': store}
    return render(request, 'polls/detail_sun.html', context)
