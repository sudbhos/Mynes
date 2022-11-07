from django.contrib import admin
from .models import student
# Register your models here.
# class Adminstudent(admin.ModelAdmin):
#     list_display = ["name","marks","amount","email"]

admin.site.register(student)