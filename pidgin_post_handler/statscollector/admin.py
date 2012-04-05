from statscollector.models import UserStatSub
from django.contrib import admin

class UserStatSubAdmin(admin.ModelAdmin):
  list_display = ['uname', 'im_services', 'time_of_sum']
  search_fields = ['im_services']

admin.site.register(UserStatSub, UserStatSubAdmin)
