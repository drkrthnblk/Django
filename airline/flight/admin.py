# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Flight, Airport
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)

#name: Rajat
#email: abc@mail.com
#password: 123456abc