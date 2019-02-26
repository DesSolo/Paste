from django.contrib import admin
from . import models


@admin.register(models.CodePaste)
class PasteAdmin(admin.ModelAdmin):
    pass
