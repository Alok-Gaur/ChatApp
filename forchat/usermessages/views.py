from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Thread
# Create your views here.


@login_required
def messages(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related(
        'chatmessage_thread').order_by('-updated')
    context = {
        'Threads': threads
    }

    if request.method == 'POST':
        logout(request)
        return redirect('userauth')

    return render(request, "ForChat.html", context)
