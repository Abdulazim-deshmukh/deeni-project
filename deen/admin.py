from django.contrib import admin
from .models import Surah, Dua, Azan

# Register your models here.
admin.site.register(Surah)
admin.site.register(Dua)
admin.site.register(Azan)