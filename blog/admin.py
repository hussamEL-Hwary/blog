from django.contrib import admin
from django.db import models
from .models import Category, Tutorial
from tinymce.widgets import TinyMCE
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Category)
admin.site.register(Tutorial, TutorialAdmin)
