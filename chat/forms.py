from django import forms
 
class ChatForm(forms.Form):
    text = forms.CharField(required=False)