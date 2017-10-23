# -*- coding: utf-8 -*-
from django.db import models
from localflavor.jp.forms import JP_PREFECTURES
from django.core.validators import MinLengthValidator

class Entry(models.Model):
    userid = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    #住所には固定長のためMinLengthValidatorを設定する
    zip1 = models.CharField(validators=[MinLengthValidator(3)],max_length=3)
    zip2 = models.CharField(validators=[MinLengthValidator(4)],max_length=4)
    #日本語様に都道府県名が自動で埋まる
    prefecture = models.CharField(choices=JP_PREFECTURES,max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    email = models.EmailField()

