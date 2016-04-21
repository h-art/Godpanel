from django.shortcuts import render
from django.http import JsonResponse
from panel.models import Employee, Allocation
from datetime import datetime


def index(request):
  return render(request, 'index.html', {})

def employees(request):
  response = [{
    'id': employee.id,
    'title': employee.full_name,
    'role': employee.role.name,
    'area': employee.area.name
  } for employee in Employee.objects.all()]

  return JsonResponse(response, safe=False)

def allocations(request):
  response = [{
    'id': allocation.id,
    'resourceId': allocation.employee.id,
    'start': allocation.start,
    # add 23:59 to end event (fixes issue for events ending 1 day before)
    'end': datetime(year=allocation.end.year, month=allocation.end.month, day=allocation.end.day, hour=23, minute=59),
    'saturation': allocation.saturation,
    'title': allocation.project.name,
    'client': allocation.project.client.name,
    'allocation_type': allocation.allocation_type
  } for allocation in Allocation.objects.all()]

  return JsonResponse(response, safe=False)
