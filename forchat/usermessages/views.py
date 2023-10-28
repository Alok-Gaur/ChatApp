from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Thread
# Create your views here.


@login_required
def messages(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related(
        'chatmessage_thread').order_by('-updated')
    context = {
        'Threads': threads
    }
    return render(request, "ForChat.html", context)
