from django.db import models

class ExpenseType(models.Model):
    ExpenseTypeName = models.CharField("Expense Type", max_length=200)

    class Meta:
        ordering = ["ExpenseTypeName"]
        verbose_name_plural = "Expense Types"

    def __str__(self):
        return self.ExpenseTypeName


class Expenses(models.Model):
    date = models.DateField('Expense Date')
    amount = models.DecimalField("Expense Amount", max_digits=5, decimal_places=2)
    payee = models.CharField("Payee", max_length=200, blank=True, null=True)
    note = models.TextField("Note", max_length=255, blank=True, null=True)
    reimbursable = models.BooleanField(null=True, blank=True)
    exp_type = models.ForeignKey(ExpenseType, verbose_name="Expense Type", on_delete="models.PROTECT", blank=True, null=True)
    receipt = models.FileField(upload_to='uploads/%Y/%m/', verbose_name="Receipt", blank=True, null=True)

    class Meta:
        ordering = ["date"]
        verbose_name_plural = "Expenses"

    def __str__(self):
        return f"{self.date} {self.payee} {self.amount}"