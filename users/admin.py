from django.contrib import admin
from .models import Profile, ContactUs



class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date')


admin.site.register(Profile)
admin.site.register(ContactUs, ContactUsAdmin)
