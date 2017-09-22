# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'SignupForm/name.html', {'form': form})
    else:
        form = NameForm()

    return render(request, 'SignupForm/name.html', {'form': form})
