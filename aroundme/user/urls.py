from django.urls import path
from user.views import *

urlpatterns = [
    path('uhome',mainhome.as_view(),name="uh1"),
    path('profile/',profileView.as_view(),name="prof"),
    path('addbio/',bioView.as_view(),name="bio"),
    path('myvlog/',vlogview.as_view(),name="vlog"),
    path('addpost/',createview.as_view(),name="apost"),
    path('cpswd/',EditPassword.as_view(),name="cpswd"),
    
    path("editbio/<int:pk>",EditView.as_view(),name="editbio"),
    path("editpost/<int:pk>",EditpostView.as_view(),name="epost"),
    path("deletepost/<int:pk>",DeletePostview.as_view(),name="dpost"),
    path("addcmnt/<int:pid>",addcomment,name="acmnt"),
    path("addlike/<int:pid>",addlike,name="alike"),
    
    
    
    
    
]