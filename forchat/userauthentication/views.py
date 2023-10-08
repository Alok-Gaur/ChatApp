from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def userauth(request):

    if request.method == 'POST':
        if request.POST.get("form_type") == 'signup':
            username = request.POST['username']
            email = request.POST['email']
            pswd = request.POST['pswd']
            pswd2 = request.POST['pswd2']

            if User.objects.filter(email=email):
                messages.warning(request, "Account Already Exist!")
                return redirect("userauth")
            elif pswd != pswd2:
                messages.warning(request, "Password Not Match")
                return redirect("userauth")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=pswd)
                user.save()
                messages.success(request, "Account Created!")
                return redirect("userauth")

        elif request.POST.get("form_type") == 'signin':
            print("old User")
    return render(request, "SignUp.html")
