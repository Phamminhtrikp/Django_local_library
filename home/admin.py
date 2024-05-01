from django.contrib import admin
from .models import myblog, Users

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'image')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'created_at', 'status')

admin.site.register(myblog,BlogAdmin)
# Register your models here.

admin.site.register(Users, UserAdmin)
