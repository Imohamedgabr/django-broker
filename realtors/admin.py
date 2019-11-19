from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email' , 'hire_date')
    list_display_links = ('id' , 'name')
    list_filter = ('name', )
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor , RealtorAdmin)