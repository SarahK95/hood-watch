from django.contrib import admin
from .models import *


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']

# Register your models here.
admin.site.register(Hood)
admin.site.register(Health,HealthAdmin)
admin.site.register(Business)
admin.site.register(Healthdepts)
admin.site.register(Police)
admin.site.register(Post)
admin.site.register(Profile)