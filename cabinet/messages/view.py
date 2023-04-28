from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import SendMessageForm
from .model import Message


def send_message_request(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = SendMessageForm(request.POST, request=request)

        if form.is_valid():
            form.save()
            return redirect('homepage')

        messages.error(request, 'Can\'t send new message. Invalid information.')

    form = SendMessageForm()

    return render(request=request, template_name='messages/send_message_template.html', context={'send_message_form': form})


def read_message_request(request, username):
    if not request.user.is_authenticated:
        return redirect('login')

    sender = User.objects.get(username=username)

    if not sender:
        return redirect('homepage')

    _messages = Message.objects.filter(sender=sender, recipient=request.user)

    return render(
        request=request,
        template_name='messages/read_message_template.html',
        context={'sender': sender, 'messages': _messages}
    )
