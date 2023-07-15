from django.contrib import admin

from . import models as analytics_models
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in analytics_models.Message._meta.fields]


admin.site.register(analytics_models.Message, MessageAdmin)
