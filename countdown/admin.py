from django.contrib import admin
from .models import Birthday


# Register your models here.
class BirthdayAdmin(admin.ModelAdmin):
    model = Birthday


admin.site.register(Birthday, BirthdayAdmin)
