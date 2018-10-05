from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _, ngettext_lazy
import datetime

message_bad_length = _('Asegurece que tenga solo 11 dígitos')
message_no_alpha = _('Asegurece que no tenga caracteres alfabéticos')
message_no_valid_date = _('Asegurece que los 6 primeros dígitos conformen una fecha válida')
message_future_date = _('Asegurece que la fecha del carnet de identidad no esté en el futuro')
message_not_blank = _('El Carnet de Identidad no puede estar en blanco')


def secure_date(cadena):
    param_year = cadena[:2]
    param_month = cadena[2:4]
    param_day = cadena[4:6]

    if int(param_month) > 12:
        return False


def ci_validate(value):
    if len(value) is 0 or value is '' or value is None:
        raise ValidationError(message=message_not_blank, code="not_blank")
    if len(value) is not 11:
        raise ValidationError(message=message_bad_length, code="bad_length")
