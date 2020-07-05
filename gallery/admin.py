from django.contrib import admin
from .models import DepartmentImage , DepartmentPostImage
# Register your models here.


class DepartmentPostImageInline(admin.TabularInline):
    model = DepartmentPostImage

class DepartmentImageAdmin(admin.ModelAdmin):
    inlines = [DepartmentPostImageInline]

admin.site.register(DepartmentImage)
admin.site.register(DepartmentPostImage)