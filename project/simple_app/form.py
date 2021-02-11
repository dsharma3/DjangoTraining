from django import forms

class ContactForm(forms.Form):
    contactname = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea(attrs={'class' : 'formGroup'}))