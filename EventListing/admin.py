from django.contrib import admin

from .models import Event, Contact, About

admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(About)