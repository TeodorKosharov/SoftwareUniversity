from django.core.exceptions import ValidationError


def egn_validator(value):
    if len(value) != 10:
        raise ValidationError('EGN must have exactly 10 digits!')
