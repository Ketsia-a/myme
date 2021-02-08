from django.contrib import admin
from .models import Profile, Problem,Tip,Department

# Register your models here.

admin.site.register(Problem)
admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(Tip)