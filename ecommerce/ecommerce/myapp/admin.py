from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(user)
admin.site.register(main_category)
admin.site.register(sub_category)
admin.site.register(product)
admin.site.register(price)
admin.site.register(color)
admin.site.register(add_cart)
admin.site.register(contact_info)
admin.site.register(billing_details)