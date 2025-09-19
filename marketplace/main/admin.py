from django.contrib import admin
from .models import Category, SubCategory, Types, Listing, Response, Order

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Types)
admin.site.register(Listing)
admin.site.register(Response)
admin.site.register(Order)
