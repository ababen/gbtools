from django import forms

from .models import Expenses, ExpenseType

class CreateForm(forms.ModelForm):

    date = forms.DateField()

    class Meta:
        model = Expenses
        fields = '__all__'


class CreateExpenseType(forms.ModelForm):

    # expense_type_name = forms.CharField()

    class Meta:
        model = ExpenseType
        fields = '__all__'