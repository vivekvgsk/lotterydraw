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

# class Home(TemplateView):
#     model=Lottery
#     template_name="home.html"

class Home(TemplateView):
    template_name = "home.html"


def result(request,*args,**kwargs):
    n=1265478
    # n=random.randint(1000000,9999999)
    lottery=Lottery.objects.filter(lottery_no=n)

    if lottery:
        print("you are lucky")
        print(lottery)
        context={"lottery":lottery}

        return render(request,"result.html",context)
    else:
        print("you are unlucky")
        print(n)
        print(lottery)
        messages.error(request, "Sorry BetterLuck NextTime")

        return render(request, "result.html")

