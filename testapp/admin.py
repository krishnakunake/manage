from django.contrib import admin

from testapp.models import Testapp_User, employee

admin.site.register(employee)
admin.site.register(Testapp_User)

