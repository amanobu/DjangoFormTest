# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm

def index(request):
    form = SignupForm()
    return render(request, 'SignupForm/entry.html', {'form': form})

def confirm(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            #もしValidationで値を変換したらなばform情報を再構成する必要があるのでたぶんＯＫのはず
            form = SignupForm(initial=form.cleaned_data)
    else:
        #POSTでないならば空のFormを作成する
        form = SignupForm()
    return render(request, 'SignupForm/confirm.html', {'form': form})

def regist(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            #もしValidationで値を変換したらなばform情報を再構成する必要があるのでたぶんＯＫのはず
            form = SignupForm(initial=form.cleaned_data)
    else:
        #POSTでないならば空のFormを作成する
        form = SignupForm()

    return render(request, 'SignupForm/fin.html', {'form': form})
