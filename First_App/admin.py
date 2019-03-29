from django.contrib import admin

# Register your models here. with Admin code
class EmpAdmin(admin.ModelAdmin):
    a=10
    B=20
    C = a + B
    pass
