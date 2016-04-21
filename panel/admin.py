from django.contrib import admin
from models import Employee, Area, Role, Client, Project, Allocation


admin.site.site_title = 'Godpanel'
admin.site.site_header = 'Godpanel'

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'area', 'role')
  list_filter = ('area', 'role')

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'client')

class AllocationAdmin(admin.ModelAdmin):
  list_display = ('start', 'end', 'saturation', 'allocation_type', 'employee', 'project')
  ordering = ('-start',)

admin.site.register(Area)
admin.site.register(Role)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Allocation, AllocationAdmin)
