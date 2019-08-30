from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, response
from django.shortcuts import render, redirect
import csv

from .models import Expenses, ExpenseType

from .forms import CreateForm


class ExpenseList(ListView):
    model = Expenses
    fields = '__all__'


class ExpenseDetail(DetailView):
    model = Expenses
    fields = '__all__'


'''
class ExpenseCreate(CreateView):
    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')
'''


class ExpenseUpdate(UpdateView):
    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')


class ExpenseDelete(DeleteView):
    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')


def create(request):
	if request.method == "POST":
		form = CreateForm(request.POST)
		if form.is_valid():
			expense = form.save(commit=False)
			# expense.author = request.user
			# expense.published_date = timezone.now()
			expense.save()
			return redirect('expenses_list')
	else:
		form = CreateForm()
	return render(request, 'expenses/expenses_create.html', {'form': form})


def download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
    expenses = Expenses.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Date', 'Payee', 'Amount', 'Note',
                     'Reimbursable?', 'Type', 'Receipt'])
    for expense in expenses:
        writer.writerow([expense.date, expense.payee, expense.amount, expense.note,
                         expense.reimbursable, expense.exp_type, expense.receipt])

    return response
