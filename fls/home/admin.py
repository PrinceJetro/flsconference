from django.contrib import admin
from .models import Registration, ContactMessage, AbstractSubmission

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'category', 'track', 'created_at')
    search_fields = ('name', 'email', 'institution', 'payment_reference')
    list_filter = ('category', 'track')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('subject',)


@admin.register(AbstractSubmission)
class AbstractSubmissionAdmin(admin.ModelAdmin):
    list_display = ('abstract_title', 'author_name', 'presentation_type', 'created_at')
    search_fields = ('author_name', 'email', 'abstract_title')
    list_filter = ('presentation_type', 'track')
