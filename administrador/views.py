from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import SignupForm


# Create your views here.


def registro(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def home(request):
    context={}
    if request.user.is_authenticated:
        request.session["usuario"]=request.user.username
        usuario=request.session["usuario"]
        context={'usuario':usuario}
    return render(request,'home.html',context)

def chao(request):
     logout(request)
     context = {}
     return render(request,'home.html',context)