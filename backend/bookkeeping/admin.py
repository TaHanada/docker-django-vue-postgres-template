from django.contrib import admin

from . import models
# Register your models here.


class EntryAdminView(admin.ModelAdmin):
    list_display = ('user', 'amount', 'notes', 'category', 'type', 'date', 'created_at')
    # raw_id_fields = ("user",)
    search_fields = ('user__email','user__username', 'amount', 'notes','category','type','date')


class EntryCategoryAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    ordering = ('name', 'type')


admin.site.register(models.Asset)
admin.site.register(models.Liability)
admin.site.register(models.Equity)
admin.site.register(models.Entry, EntryAdminView)
admin.site.register(models.EntryCategory, EntryCategoryAdminView)
