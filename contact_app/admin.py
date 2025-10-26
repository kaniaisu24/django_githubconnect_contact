# from django.contrib import admin
# from .models import Contact

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'submitted_at')
#     readonly_fields = ('submitted_at',)

from django.contrib import admin
from .models import ContactSubmission

admin.site.register(ContactSubmission)


