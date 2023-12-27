from django.contrib import admin
from  .models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['Name','Email','Mobno','password','Adhaar','token','user_category']
   
