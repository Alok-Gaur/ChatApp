from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Thread
# Create your views here.


@login_required
def messages(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related(
        'chatmessage_thread').order_by("updated")[::-1]
    context = {
        'Threads': threads
    }
    # print('The Message is: ', request.POST.get('id'))
    if request.method == 'POST':
        if request.POST.get('form_type') == 'logout':
            logout(request)
            return redirect('userauth')
        else:
            search = request.POST.get('search-box')
            try:
                try:
                    result = User.objects.by_user(username=search)
                except:
                    result = User.objects.get(email=search)
            except:
                return render(request, "ForChat.html", context)
            print("the search users are", result)

            context['search'] = search

    return render(request, "ForChat.html", context)
