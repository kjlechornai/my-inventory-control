from django import forms
from . models import IssuedItem

class IssueModelForm(forms.ModelForm):
    class Meta:
        model = IssuedItem
        fields = '__all__'