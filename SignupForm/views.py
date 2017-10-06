# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm,SignupForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()

    return render(request, 'SignupForm/name.html', {'form': form})

def entry(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SignupForm()

    return render(request, 'SignupForm/entry.html', {'form': form})
