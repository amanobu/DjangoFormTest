# -*- coding: utf-8 -*-
from django import forms
from django.forms import CharField
from .models import Entry
from .validator import *
import re
#国際化に向けてこのようにした方が良いらしい
from django.utils.translation import gettext as _

class NameForm(forms.Form):
    your_name = forms.CharField(label = 'お名前は？' ,max_length=100)

    def clean(self):
        #cleand_dataには入力チェックが通った物が入っている
        name = self.cleaned_data['your_name']
        if name.find('テスト') == -1:
            raise forms.ValidationError("入力エラー。「テスト」って入ってないよ")
        else:
            return name

class SignupForm(forms.ModelForm):
    class Meta:
        #モデルの指定
        model = Entry
        #すべての項目を使うので'__all__'
        fields = '__all__'
        #ラベルの定義
        labels = {
            'fname':'姓',
            'lname':'名',
            'zip1':'郵便番号1',
            'zip2':'郵便番号2',
            'prefecture':'都道府県名',
            'address1':'住所1',
            'address2':'住所2',
            'address3':'住所3',
            'email':'メールアドレス'
            }
    zip1 = CharField(validators=[validate_zip1])
    zip2 = CharField(validators=[validate_zip2])

    
    #強制的にclass="form-control"をくっつける
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    #独自バリデーション:モデルの検証
    def clean(self):
        name = self.cleaned_data['fname'] + self.cleaned_data['lname']
        if len(name) > 8:
            raise forms.ValidationError({'lname': _(u'姓名あわせて８文字以上だよ'),'fname': _(u'姓名あわせて８文字以上だよ')})

        

