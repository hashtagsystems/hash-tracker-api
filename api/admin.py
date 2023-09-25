from django.contrib import admin
from api.models import Category,Project,Collection,Environment

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Collection)
admin.site.register(Environment)
