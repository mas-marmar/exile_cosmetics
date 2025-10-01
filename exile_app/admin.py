from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Wishlists)
admin.site.register(Products)
admin.site.register(Reviews)
admin.site.register(Discounts)
admin.site.register(Orders)