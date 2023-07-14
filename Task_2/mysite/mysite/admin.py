from django.contrib import admin
from django_otp.plugins.otp_totp.models import TOTPDevice

admin.site.register(TOTPDevice)
