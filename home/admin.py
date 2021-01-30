from django.contrib import admin
from .models import Clothes
from .models import Category

# Register your models here.
admin.site.register(Clothes)
admin.site.register(Category)
