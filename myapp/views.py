from django.shortcuts import render ,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic.edit import CreateView ,DeleteView,UpdateView
from .forms import ContactForm,BusnessForm,PoliticsForm,Signup ,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate, logout
from .models import Contact,Politics,Business
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from django.views import View


# Create your views here.

# Create your views here.
def Home(request):
    form=Politics.objects.all()
    return render(request,'myapp/index.html',{'form':form})

def Busnesshome(request):
    form=Business.objects.all()
    return render(request,'myapp/busness.html',{'forms':form}) 

def PoliticsHome(request):
    form=Politics.objects.all()
    return render(request,'myapp/politics.html',{'form':form})
class BusnessDetail(DetailView):
    template_name='myapp/busnessDetail.html'
    model=Business

class PoliticsDetail(DetailView):
    template_name='myapp/politicsdetail.html'
    model=Politics

# contact
class ContactUs(CreateView):
    form_class=ContactForm
    template_name='myapp/contact.html'
    success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#Busnesss 
@method_decorator(login_required,name='dispatch')
class Busnesssclass(CreateView):
    form_class=BusnessForm
    template_name='author/Busness.html'
    success_url='/busness/'
   
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
#politics
@method_decorator(login_required,name='dispatch')
class Politicsclass(CreateView):
    form_class=PoliticsForm
    template_name='author/politics.html'
    success_url='/politics/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  

def register_user(request):
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()    
    else:
        form=Signup()
    return render(request,'myapp/signup.html',{'form':form})           

# login function
class Loginclass(LoginView):
    template_name='myapp/login.html'
    authentication_form=LoginForm

def Profile(request):
    return render(request,'myapp/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@method_decorator(login_required,name='dispatch')
class UpdateBusness(UpdateView):
    model=Business
    fields=['title','slug','date','content','image','author']
    template_name='author/updateBusness.html'
    success_url='/updatebusness/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




def DeleteBusness(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Business.objects.get(pk=id)
      pi.delete()
    return redirect('/')
  else:
    return HttpResponseRedirect('/login/')   
    # end 


@method_decorator(login_required,name='dispatch')
class UpdatePolitics(UpdateView):
    model=Politics
    fields=['title','slug','date','content','image','author']
    template_name='author/updatePolitics.html'
    success_url='/updatepolitics/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
@method_decorator(login_required,name='dispatch')
class DeletePolitics(DeleteView):
    model=Politics
    success_url='/busness_edit/'        
@login_required()
def Business_edit(request):
    form=Business.objects.all()
    return render(request,'author/BusnessEdit.html',{'form':form})
@login_required()
def Politics_edit(request):
    form=Politics.objects.all()
    return render(request,'author/politicsEdit.html',{'form':form}) 

