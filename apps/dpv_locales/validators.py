from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import datetime

# Messages
message_aa = _("Debe seguir el patron de XX/XX donde se sustituyen las X por numeros")
message_future_year = _("El acuerdo o acta no puede ser de un anno futuro.")
message_format_bad = _("El acuerdo o acta debe contener al menos y solo un slash '/' ")
message_year_bad = _("El anno debe tener el siguiente formato XX o XXXX")


# Validators
def validate_acta_acuerdo(value):
    splited = value.split('/')
    if len(splited) is not 2:
        raise ValidationError(message=message_format_bad, code="format_bad")
    if len(splited[-1]) is not 2 or len(splited[-1]) is not 4:
        raise ValidationError(message=message_year_bad, code="year_bad")
    splited_year = int(splited[-1])
    if splited_year < datetime.date.today().year:
        raise ValidationError(message=message_future_year, code="future_year")

