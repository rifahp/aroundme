from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import signupForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

class home(TemplateView):
    template_name="mainhome.html"
    # def get(self,request,*args,**kwargs):
    #     return render(request,"mainhome.html")
    
# class Signup(View):
#     def get(self,request,*args,**kwargs):
#         f=signupForm()
#         return render(request,"signup.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         f=signupForm(data=request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request,"user registration successfull")
#             return redirect("m")
#         else:
#              messages.error(request,"user Registration failed")
#              return render(request,"signup.html",{"form":f})

class Signup(CreateView):
    form_class=signupForm
    template_name="signup.html"
    model=User
    success_url=reverse_lazy("m")
         
         
# class loginview(View):
#     def get(self,req):
#             b=LoginForm()
#             user=req.user
#             return render(req,"login.html",{"form":b,"c":user})
    # def post(self,req,*args,**kwargs):
    #     b=LoginForm(data=req.POST)
    #     if b.is_valid():
    #         un=b.cleaned_data.get("username")
    #         pw=b.cleaned_data.get("password")
    #         user=authenticate(req,username=un,password=pw)
    #         if user:
    #             login(req,user)
    #             messages.success(req,"LOGIN SUCCESSFULL")
    #             return redirect("uh1")
    #         else:
    #             messages.error(req,"LOGIN failed!!")
    #             return redirect("login")
    #     else:
    #         return render(req,"login.html",{"form":b})

class loginview(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,req,*args,**kwargs):
        b=LoginForm(data=req.POST)
        if b.is_valid():
            un=b.cleaned_data.get("username")
            pw=b.cleaned_data.get("password")
            user=authenticate(req,username=un,password=pw)
            if user:
                login(req,user)
                messages.success(req,"LOGIN SUCCESSFULL")
                return redirect("uh1")
            else:
                messages.error(req,"LOGIN failed!!")
                return redirect("login")
        else:
            return render(req,"login.html",{"form":b})
        
class logout(View):
    def get(self,request):
        logout(request)
        return redirect("login")
    
    
            
    




    