from django.contrib import admin
from .models import Location, Shelf, Project, Department, Requestor, Work

admin.site.register(Location)
admin.site.register(Shelf)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Requestor)
admin.site.register(Work)