from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from ..messages.model import Message


def homepage_request(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users_ids = Message.objects.filter(recipient=request.user).values('sender').distinct()
    users = User.objects.filter(id__in=users_ids)

    return render(request=request, template_name='homepage/template.html', context={'users': users})
