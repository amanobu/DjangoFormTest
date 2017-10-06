# -*- coding: utf-8 -*-
from django.db import models
from localflavor.jp.forms import JP_PREFECTURES

class Entry(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    zip1 = models.CharField(max_length=3)
    zip2 = models.CharField(max_length=4)
    #日本語様に都道府県名が自動で埋まる
    prefecture = models.CharField(choices=JP_PREFECTURES,max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    email = models.EmailField()

