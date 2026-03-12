from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import ExpenseForm, SearchForm
from .models import Expense

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "add.html", {"form": form})

def expense_list(request):
    expenses = Expense.objects.order_by("-date", "-id")
    return render(request, "list.html", {"expenses": expenses})

def search_expenses(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data.get("q")
        date = form.cleaned_data.get("date")
        qs = Expense.objects.all()
        if q:
            qs = qs.filter(description__icontains=q)
        if date:
            qs = qs.filter(date=date)
        results = qs.order_by("-date", "-id")
    return render(request, "search.html", {"form": form, "results": results})