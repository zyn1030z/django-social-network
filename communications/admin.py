from django.contrib import admin

# Register your models here.
from communications.models import Room,Message

admin.site.register(Room)
admin.site.register(Message)
