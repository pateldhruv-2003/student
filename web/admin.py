from django.contrib import admin
from.models import category
from.models import student
from.models import product
from.models import contact
from.models import fees

# Register your models here.
admin.site.register(category)
admin.site.register(student)
admin.site.register(product)
admin.site.register(contact)
admin.site.register(fees)
