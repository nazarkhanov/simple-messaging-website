from django.shortcuts import render, redirect
from django.contrib import messages
from .form import RegisterForm


def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered.')
            return redirect('login')

        messages.error(request, 'Can\'t register. Invalid information.')

    form = RegisterForm()

    return render(request=request, template_name='registration/template.html', context={'register_form': form})
