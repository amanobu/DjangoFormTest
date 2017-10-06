from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

def validate_number(value):
    if not value.isdigit():
        raise ValidationError(
            _('%(value)s is not number'),
            params={'value': value},
        )

def validate_zip1(value):
    if validate_number(value):
        num = int(value)
        if 100 >= num or num > 1000:
            raise ValidationError(
                _('%(value)s is invalid'),
                params={'value': value},
            )

def validate_zip2(value):
    if validate_number(value):
        num = int(value)
        if 100 >= num or num > 10000:
            raise ValidationError(
                _('%(value)s is invalid'),
                params={'value': value},
            )
    
