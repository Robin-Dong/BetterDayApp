from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.DailyEnglish)
admin.site.register(models.DailyQuote)
admin.site.register(models.DailyImg)
