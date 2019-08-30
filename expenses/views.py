from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import csv

from .models import Expenses, ExpenseType

from .forms import CreateForm, CreateExpenseType


class ExpenseList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Expenses
    fields = '__all__'


class ExpenseDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Expenses
    fields = '__all__'


'''
class ExpenseCreate(CreateView):
    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')
'''


class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')


class ExpenseDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses_list')


@login_required
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
        add_exp_type = CreateExpenseType()
    return render(request, 'expenses/expenses_create.html', {'form': form, 'add_exp_type': add_exp_type})


@login_required
def add_expense_type(request):
    if request.method == 'POST':
        form = CreateExpenseType(request.POST)
        if form.is_valid():
            expense_type = form.save(commit=False)
            expense_type.save()
            return redirect('expenses_create')
    return HttpResponseRedirect('../create')


@login_required
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
