from django.contrib import admin
from .models import Doctors
from .models import User
# Register your models here.
admin.site.register(Doctors)
admin.site.register(User)