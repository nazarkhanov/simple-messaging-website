from django.urls import path

from .homepage.view import homepage_request
from .messages.view import send_message_request, read_message_request
from .registration.view import register_request
from .authentication.view import login_request, logout_request
from .dump.view import dump_request

urlpatterns = [
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout', logout_request, name='logout'),

    path('', homepage_request, name='homepage'),
    path('send-message', send_message_request, name='send-message'),
    path('read-message/<str:username>', read_message_request, name='read-message'),

    path('dbdump', dump_request, name='dbdump'),
]
