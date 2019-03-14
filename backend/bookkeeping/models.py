from django.db import models
from backend.users.models import User

# These are the 5 "Accounts" of a General Ledger.
# 1. Assets
# 2. Liabilities
# 3. Equity
# 4. Income
# 5. Expense

ENTRY_TYPES = (
    (0, 'Expense'),
    (1, 'Income'),
)


class Asset(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)

class Liability(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)

class Equity(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)

class Entry(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    category = models.ForeignKey(
        'bookkeeping.EntryCategory',  on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    notes = models.CharField(max_length=1000)
    type = models.IntegerField(choices=ENTRY_TYPES, null=False, blank=False)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)
# class Income(Entry):
#     class Meta:
#         verbose_name = "income"


# class Expense(Entry):
#     class Meta:
#         verbose_name = "expense"


class EntryCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    type = models.IntegerField(choices=ENTRY_TYPES, null=False, blank=False)