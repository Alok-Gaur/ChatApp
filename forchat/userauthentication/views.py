from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
# Create your views here.


def userauth(request):

    if request.method == 'POST':
        if request.POST.get("form_type") == 'signup':
            username = request.POST['username']
            email = request.POST['email']
            pswd = request.POST['pswd']
            pswd2 = request.POST['pswd2']

            if User.objects.filter(username=username):
                messages.warning(
                    request, f'Username {username} is already used!')
            elif User.objects.filter(email=email):
                messages.warning(request, "Account Already Exist!")
                # return redirect("userauth")
            elif pswd != pswd2:
                messages.warning(request, "Password Not Match")
                # return redirect("userauth")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=pswd)
                user.save()
                messages.success(request, "Account Created!")
                # return redirect("userauth")

        # elif request.POST.get("form_type") == 'signin':
        else:
            nmauth = request.POST['nmauth']
            pswd = request.POST['pswd']
            user = None

            if User.objects.filter(username=nmauth):
                user = authenticate(request, username=nmauth, password=pswd)
            else:
                try:
                    uname = User.objects.get(email=nmauth).username
                    print(uname)
                    user = authenticate(request, username=uname, password=pswd)
                except:
                    messages.info(request, "Enter correct email address")

            if user is not None:
                form = login(request, user)
                print(form)
                # messages.success(request, f'Welcome {user.username.title()}!')
                return redirect('message/')
            elif User.objects.filter(Q(email=nmauth) | Q(username=nmauth)):
                messages.info(request, "Incorrect Password!!")
            else:
                messages.info(
                    request, f'Account does not exist with username or email "{nmauth}"')

    return render(request, "SignUp.html")
