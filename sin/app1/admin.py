from django.contrib import admin
from .models import Login

# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ['id','first','middle','last','dob','email','mobile','skills','gender','file']
admin.site.register(Login,LogAdmin)
