from django.contrib import admin
from aliance.models import Person, Applications, MyModel
from aliance.views import export_csv, export_xls
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    actions = [export_csv, export_xls]


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Applications, MyModelAdmin)
admin.site.register(Person)


