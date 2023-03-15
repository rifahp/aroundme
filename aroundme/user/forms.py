from django import forms
from .models import Bio,Posts,Comments

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude={"user"}
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }
        
class PchangeForm(forms.Form):
    old_password=forms.CharField(max_length=100,label="old password",widget=forms.PasswordInput)
    new_password=forms.CharField(max_length=100,label="new password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=100,label="confirm password",widget=forms.PasswordInput)
    
class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image","caption"]
        widgets={
            # "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"})
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"})
        }
        
    
    