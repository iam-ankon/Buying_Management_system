from django.contrib import admin
from .models import SampleFollowUp, SampleComment, Reminder

@admin.register(SampleFollowUp)
class SampleFollowUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'status')
    search_fields = ('name', 'status')
    list_filter = ('date', 'status')

@admin.register(SampleComment)
class SampleCommentAdmin(admin.ModelAdmin):
    list_display = ('follow_up', 'created_at')
    search_fields = ('follow_up__name',)
    list_filter = ('created_at',)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'reminder_date')
    search_fields = ('title',)
    list_filter = ('reminder_date',)
