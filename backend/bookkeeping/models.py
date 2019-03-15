from django.db import models
from django.contrib.auth import get_user_model

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
        get_user_model(),  on_delete=models.CASCADE)


class Liability(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    user = models.ForeignKey(
        get_user_model(),  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Liablility"
        verbose_name_plural = "Liabilities"


class Equity(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    user = models.ForeignKey(
        get_user_model(),  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Equities"


class Entry(models.Model):
    # id = models.AutoField(primey_key=True)
    amount = models.FloatField(blank=False, null=False)
    category = models.ForeignKey(
        'bookkeeping.EntryCategory',  on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.CharField(max_length=1000)
    type = models.IntegerField(choices=ENTRY_TYPES, null=False, blank=False)
    user = models.ForeignKey(
        get_user_model(),  on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"


class EntryCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    type = models.IntegerField(choices=ENTRY_TYPES, null=False, blank=False)

    def __str__(self):
        return self.name + " (" + ENTRY_TYPES[self.type][1] + ")"

    class Meta:
        verbose_name = "Entry Category"
        verbose_name_plural = "Entry Categories"
