from django.contrib import admin
from .models import Ticket, Department, UserQuery

admin.site.register(Ticket)
admin.site.register(Department)
admin.site.register(UserQuery)