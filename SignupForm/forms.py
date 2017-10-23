# -*- coding: utf-8 -*-
from django import forms
from django.forms import CharField
from .models import Entry
from .validator import *
import re
from .util import numZEN2HAN
#国際化に向けてこのようにした方が良いらしい
from django.utils.translation import gettext as _

class SignupForm(forms.ModelForm):
    class Meta:
        #モデルの指定
        model = Entry
        #すべての項目を使うので'__all__'で良いのだが、あまりやらない方が良いらしいとDjangoチュートリアルに記載されていた
        fields = '__all__'
        #ラベルの定義
        labels = {
            'userid':'ご希望のUSER ID',
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
    
    #強制的にclass="form-control"をくっつける
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    #各フィールドの個別チェック
    def clean_zip1(self):
        zip1 = self.cleaned_data.get('zip1')
        if zip1 and not validate_zip1(zip1):
            raise forms.ValidationError(_('正しく入力してよ'))
        else:
            #値の変換
            tmp_zip1 = numZEN2HAN(zip1)
            self.cleaned_data['zip1'] = tmp_zip1
        #値を変換したらclean_dataに反映する為新しい値をreturnする必要がある
        return tmp_zip1

    def clean_zip2(self):
        zip2 = self.cleaned_data.get('zip2')
        if zip2 and not validate_zip2(zip2):
            raise forms.ValidationError(_('正しく入力してよ'))
        else:
            tmp_zip2 = numZEN2HAN(zip2)
            self.cleaned_data['zip2'] = tmp_zip2
        return tmp_zip2

    #独自バリデーション:モデルの検証
    def clean(self):
        #姓名合わせて～文字の検証
         if not validate_name(self.cleaned_data.get('fname'), self.cleaned_data.get('lname')):
            raise forms.ValidationError({'lname': _(u'姓名あわせて2文字以上、８文字以下だよ'),'fname': _(u'姓名あわせて2文字以上、８文字以下だよ')})

