from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["description", "amount", "date"]
        labels = {
            "date": "Date (DD-MM-YYYY)",
        }

class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="Description contains")
    date = forms.DateField(required=False, label="Date (DD-MM-YYYY)")