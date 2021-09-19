from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import myUserForm

# Create your views here.
def HomeView(request):
    template_name='AuthenticationApp/home.html'
    context={}
    return render(request,template_name,context)

def RegisterView(request):
    form=myUserForm()
    if request.method =='POST':
        form = myUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name='AuthenticationApp/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def loginView(request):
    if request.method =='POST':
        print('post')
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        print(u,p)
        user=authenticate(username=u,password=p)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('userpage')
        else:
            messages.error(request,'Invalid Credentials')

    print('get')
    template_name='AuthenticationApp/login.html'
    context={}
    return render(request,template_name,context)

def logOutView(request):
    logout(request)
    return redirect('home')

def userPageView(request):
    template_name='AuthenticationApp/userpage.html'
    context={}
    return render(request,template_name,context)

def changePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method=='POST':
        form = PasswordChangeForm(request.user,request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user) #this line keeps u logged in after change password
            messages.success(request,'password changed successfuly')
            return redirect('userpage')
        else:
            messages.error(request,'check password')
    template_name='AuthenticationApp/changepass.html'
    context={'form':form}
    return render(request,template_name,context)