from django.db import models


class Expenses(models.Model):
    date = models.DateTimeField('expense date')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payee = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    # receipt = models.FileField(upload_to='uploads/%Y/%m/%d/')


class ExpenseType(models.Model):
    ExpenseTypeName = models.CharField(max_length=200)