from django import forms
from django.forms import ModelForm

from studentbasic.models import Primary


class PrimaryCreateForm(forms.ModelForm):
    class Meta:
        model = Primary
        fields = ['admin_no', 'name', 'kidato', 'darasa', 'dob',
                  'kcpe_mark', 'county', 'year_of_completion', 'parent_contact'
                  ]
