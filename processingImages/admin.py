from django.contrib import admin

# Register your models here.
from .models import Signal

from .models import CompositeModel

admin.site.register(CompositeModel)
admin.site.register(Signal)