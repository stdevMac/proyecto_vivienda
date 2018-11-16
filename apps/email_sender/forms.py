from django import forms
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator


class EmailForm(forms.Form):
    from_email = forms.CharField(max_length=255, label="From")
    cc_email = forms.CharField(max_length=511, label="CC")
    bcc_email = forms.CharField(max_length=511, label="BCC")
    recipients_email = forms.CharField(max_length=756, label="To")
    subject_email = forms.CharField(max_length=200, label="Asunto")
    body_email = forms.CharField(max_length=1000, label="Mensaje", widget=(forms.Textarea(attrs={"class": ""})))


class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(max_length=1000, label="Mensaje", widget=(forms.Textarea(attrs={"class": ""})))