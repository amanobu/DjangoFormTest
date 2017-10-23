# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm

def entry(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            #もしValidationで値を変換したらなばform情報を再構成する必要があるのでたぶんＯＫのはず
            form = SignupForm(initial=form.cleaned_data)
    else:
        #POSTでないならば空のFormを作成する
        form = SignupForm()

    return render(request, 'SignupForm/entry.html', {'form': form})
