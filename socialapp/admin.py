from django.contrib import admin

from .models import QRCode, Visitor

admin.site.register(QRCode)
admin.site.register(Visitor)
