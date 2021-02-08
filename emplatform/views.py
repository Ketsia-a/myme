from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from .models import  Profile,Problem,Tip,Department
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import ProblemForm,TipForm
from django.contrib.auth import authenticate,login
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def home(request): 

    return render(request,'home.html')

def index(request): 
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form.save()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})    

@login_required(login_url='login')
def profile(request, username):
    problems = profile.problems.all()
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
  
    context = {
        'prof_form': prof_form,
        'cards': cards,
    }
    return render(request, 'profile.html', context)  

def problem(request):
    problems= Problem.objects.all()
    if request.method == "POST":
        form = ProblemForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.status = request.user.profile.status
            problem.save()
        return redirect('home')
    else:
        form = ProblemForm()
    context = {
        'form': form,
        'problems': problems,
    }    

    return render(request,'problem.html', context)        
def tip(request, pk):
    problem = Problem.objects.get(id = pk)
    current_user = request.user
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.problem = image
            tip.user = request.user.profile
            tip.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = TipForm()
    
    context = {
        'form': form,
        'problem':problem,
    }

    return render(request, 'problem.html', context)
class ProblemUpdateView(UpdateView):
    model = Problem
    template_name = 'problem.html'   
    fields= ['names', 'description','image','department']  
    success_url = ('/')  

def updateproblem(request):
    form = ProblemForm()
    context = {'form' : form}
    return render(request, 'problem.html', context)    

class ProblemDeleteView(DeleteView):
    model = Problem
    template_name = 'delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'delete.html', context )

def deleteproblem(request):
    context = {'object:title' : problem}
    return render(request, 'delete.html', context)
