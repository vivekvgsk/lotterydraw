from django.urls import path
from .views import Registration,SignInView,SignoutView,Home,result

urlpatterns = [
    path("signup",Registration.as_view(),name="signup"),
    path("signin",SignInView.as_view(),name="signin"),
    path("signout",SignoutView.as_view(),name="signout"),
    path("home",Home.as_view(),name="home"),
    path("result",result,name="result")

]