from django.contrib import admin
from .models import Resume,Education,experiance,certification,awards

# Register your models here.

admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(experiance)
admin.site.register(certification)
admin.site.register(awards)