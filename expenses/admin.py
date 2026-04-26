from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'notes')
    search_fields = ('title', 'category')