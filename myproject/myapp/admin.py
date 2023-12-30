from django.contrib import admin
from  .models import User,AdminUser,SuperAdmin

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['Name','Email','Mobno','password','Adhaar','token','user_category']

@admin.register(SuperAdmin)
class SuperAdminUser(admin.ModelAdmin):
    list_display = ['Username','Password']

@admin.register(AdminUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['Name','Email','Mobno','password','user_category','token']
   
