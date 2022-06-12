from django.contrib import admin
from .models import TestMessage

@admin.register(TestMessage)
class TestMessageAdmin(admin.ModelAdmin):
    pass
