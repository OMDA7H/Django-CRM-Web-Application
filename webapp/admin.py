from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass