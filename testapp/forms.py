from django import forms

from .models import User
'''
class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_fio',)
        error_messages={'required': ''}

'''

class NameForm(forms.Form):
    name = forms.CharField(max_length=100, error_messages={'required': ''})