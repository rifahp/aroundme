from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from django.contrib import messages
from .forms import BioForm,PchangeForm,PostForm,CommentForm
from .models import Bio,Posts,Comments
from django.contrib.auth import authenticate,logout




# Create your views here
class mainhome(CreateView):
    template_name="userhome.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("uh1")
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Post uploaded")
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.all().order_by('-datetime')
        context["cform"]=CommentForm()
        context["comments"]=Comments.objects.all()
        
        return context
    
    
    
class createview(CreateView):
    form_class=PostForm
    template_name="add.html"
    model=Posts
    success_url=reverse_lazy("uh1")
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Post uploaded")
        self.object=form.save()
        return super().form_valid(form)

    
    

    
# class mainhome(View):
#      def get(self,request,*args,**kwargs):
#         return render(request,"userhome.html")
     
class profileView(TemplateView):
    template_name="profile.html"
    pk_url_kwargs="pk"
    
    
    
    
class bioView(CreateView):
    form_class=BioForm
    template_name="Bio.html"
    model=Bio
    success_url=reverse_lazy("prof")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,'Bio.html')
        return super().form_valid(form)
    
class EditView(UpdateView):
    form_class=BioForm
    model=Bio
    template_name="editbio.html"
    success_url=reverse_lazy("prof")
    pk_url_kwargs="pk"
    
class EditPassword(FormView):
    template_name="change password.html"
    form_class=PchangeForm
    def post(self,request,*args,**kwargs):
        form_data=PchangeForm(data=request.POST)  
        if form_data.is_valid():
           current=form_data.cleaned_data.get("old_password")
           new=form_data.cleaned_data.get("new_password")
           confirm=form_data.cleaned_data.get("confirm_password")
           print(current)
           user=authenticate(request,username=request.user.username,password=current)
           if user:  
              if new==confirm:
               user.set_password(new)
               user.save()
               messages.success(request,"password changed")
               logout(request)
               return redirect("login")
              else:
                messages.error(request,"password mismatches!!!")
                return redirect("cpswd")
           else:
                messages.success(request,"Incorrect Password")
                return redirect("cpswd")
        else:
                return render(request,"change password.html",{"form":form_data})
            
            
class vlogview(TemplateView):
    template_name="vlogs.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Posts.objects.filter(user=self.request.user)
        return context


class EditpostView(UpdateView):
    template_name="editpost.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("apost")
    pk_url_kwargs="pk"
    
    
# class postdeleteview(View):
#       def get(self,req,*args,**kwargs):  
#             id=kwargs.get("pk")
#             post=Posts.objects.get(id=id)
#             post.delete()
#             messages.success(req,"post removed")
#             return redirect("uh1")

# using deleteview post
class DeletePostview(DeleteView):
    model=Posts
    template_name="deletepost.html"
    success_url=reverse_lazy("vlog")


def addcomment(request,*args,**kwargs):
    if request.method=="POST":
        pid=kwargs.get("pid")
        post=Posts.objects.get(id=pid)
        user=request.user
        cmnt=request.POST.get("comment")
        Comments.objects.create(comment=cmnt,user=user,post=post)
        return redirect("uh1")

def addlike(request,*args,**kwargs):
    pid=kwargs.get("pid")
    post=Posts.objects.get(id=pid)
    user=request.user
    post.likes.add(user)
    post.save()
    return redirect("uh1")     
    

    



   
