# -*- coding: utf-8 -*-
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label = 'お名前は？' ,max_length=100)

    def clean(self):
        name = self.cleaned_data['your_name']
        if name.find('テスト') == -1:
            raise forms.ValidationError("入力エラー。「テスト」って入ってないよ")
        return name

