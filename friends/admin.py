from django.contrib import admin

# Register your models here.
from friends.models import Friend, CustomNotification

admin.site.register(Friend)
admin.site.register(CustomNotification)
