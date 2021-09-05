from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Lottery
from .forms import UserRegisterForm,LoginForm
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import random
# Create your views here.

class Registration(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("signin")


class SignInView(TemplateView):
    model=User
    form_class=LoginForm
    template_name="login.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request, "Invalid User")
                return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

class SignoutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



class Home(TemplateView):
    template_name = "home.html"


# def result(request,*args,**kwargs):

#     # n=random.randint(1000000,9999999)
#     lottery=Lottery.objects.get(lottery_no=n)
#
#     if lottery:
#         print("you are lucky")
#         print(lottery)
#
#         return render(request,"result.html",{"lottery":lottery})
#     else:
#         print("you are unlucky")
#         print(n)
#         print(lottery)
#         messages.error(request, "Sorry BetterLuck NextTime")
#
#         return render(request, "result.html")




def result(request,*args,**kwargs):
    lottery_no=Lottery.objects.all() #for fetching all lottery objects from model
    rs=random.choices(lottery_no, weights=(2, 3, 30, 40, 50,1), k=1) # for creating a random choice from the set of lotteries
    # print("random selection") #for checking
    # print(rs) #for checking

    lottery=Lottery.objects.get(lottery_no=rs[0]) # for fetching the value from the random created list

    if lottery.lottery_price ==0:
        # print("you are unlucky") #for checking
        # print(lottery.lottery_no) #for checking
        # print(lottery) #for checking
        messages.error(request, "Better Try NextTime")
        return render(request, "result.html")

    else:
        # print("you are lucky") #for checking
        # print(lottery) #for checking

        return render(request, "result.html", {"lottery": lottery})

