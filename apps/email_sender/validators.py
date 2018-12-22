from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address, RegexValidator


validate_fqdn = RegexValidator('^[a-z0-9äöüéàèáéíóúüñ][.]+[a-z]$', message="Eso no puede ser un dominio válido.", code="not_valid_fqdn")


def validate_ip46_fqdn_address(value):
    pass