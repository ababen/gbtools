from django import forms

from .models import Expenses

class CreateForm(forms.ModelForm):

    date = forms.DateField()

    class Meta:
        model = Expenses
        fields = '__all__'