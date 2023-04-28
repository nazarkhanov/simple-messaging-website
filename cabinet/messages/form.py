from django import forms
from django.contrib.auth.models import User
from .model import Message


class SendMessageForm(forms.Form):
    recipient = forms.CharField(label='recipient')
    content = forms.CharField(label='content')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SendMessageForm, self).__init__(*args, **kwargs)

    def clean_recipient(self):
        username = self.cleaned_data['recipient']

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('User does not exist.')

        return username

    def save(self):
        sender = self.request.user
        recipient = User.objects.get(username=self.cleaned_data['recipient'])

        if sender == recipient:
            return None

        content = self.cleaned_data['content']
        message = Message(sender=sender, recipient=recipient, content=content)

        message.save()

        return message
