from django.shortcuts import render

# Create your views here.

def i1(request):
    context={}
    return render(request, 'i1.html', context)