from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


MATERIAL_CHOICES = (
    ('P', 'Project Material'),
    ('B', 'Borrowed')
)


class CheckoutForm(forms.Form):
    work_to_be_done = forms.CharField()
    work_location = forms.CharField(required=False)
    project = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    to_be_collected_by = forms.CharField(required=False)
    project_material_or_borrowed = forms.ChoiceField(
        widget=forms.RadioSelect, choices=MATERIAL_CHOICES)
    department = forms.CharField()