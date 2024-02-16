from django.contrib import admin
from .models import UserComments
# Register your models here.
admin.site.register(UserComments)  # Register with the custom admin class
