from django.contrib import admin
from .models import TB_FITBIT, TB_MEMBER, TB_SESSION_RESULT
# Register your models here.

admin.site.register(TB_FITBIT)
admin.site.register(TB_MEMBER)
admin.site.register(TB_SESSION_RESULT)