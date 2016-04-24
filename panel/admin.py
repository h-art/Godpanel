from django.contrib import admin
from panel.models import Employee, Area, Role, Client, Project, Allocation


admin.site.site_title = 'Godpanel'
admin.site.site_header = 'Godpanel'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'area', 'role')
    list_filter = ('area', 'role')
    ordering = ('last_name',)


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
