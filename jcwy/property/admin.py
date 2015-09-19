from django.contrib import admin
from .models import Members 


class MembersAdmin(admin.ModelAdmin):
    list_display = ['member_id', 'member_name', 'pwd', 'regist_date']
    search_fields = ['member_name']
    ordering = ['-member_id']
    list_filter = ['regist_date']

admin.site.register(Members, MembersAdmin)
