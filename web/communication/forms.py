# communication/forms.py
from django import forms
 
class SendMessageForm(forms.Form):
    content = forms.CharField(label='Message Content', widget=forms.Textarea)
