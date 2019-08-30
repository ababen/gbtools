from django.contrib import admin

from .models import Expenses, ExpenseType

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('date', 'payee', 'amount')
    list_filter = ('date', 'payee', 'exp_type', 'reimbursable')

admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(ExpenseType)