from django.contrib import admin

from orm_queries.models import Dealership, Brand, Model, Car

# Register your models here.


class GeneralAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dealership, GeneralAdmin)
admin.site.register(Brand, GeneralAdmin)
admin.site.register(Model, GeneralAdmin)
admin.site.register(Car, GeneralAdmin)
