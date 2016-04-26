from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, JsonResponse
from godpanel.models import Employee, Allocation
from django.core.urlresolvers import reverse
from datetime import datetime


def index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html', {})
    else:
        return redirect('%s%s' % (reverse('admin:login'), '?next=%s' % (reverse('godpanel.frontpage'))))


def employees(request):
    response = [{
        'id': employee.id,
        'title': ' '.join([employee.first_name, employee.last_name]),
        'role': employee.role.name,
        'area': employee.area.name
    } for employee in Employee.objects.all()]

    if request.user.is_authenticated():
        return JsonResponse(response, safe=False)
    else:
        return HttpResponseForbidden('You must authenticate')


def allocations(request):
    response = [{
        'id': allocation.id,
        'resourceId': allocation.employee.id,
        'start': allocation.start,
        # add 23:59 to end event (fixes issue for events ending 1 day before)
        'end': datetime(year=allocation.end.year,
                        month=allocation.end.month,
                        day=allocation.end.day,
                        hour=23, minute=59),
        'saturation': allocation.saturation,
        'title': allocation.project.name,
        'client': allocation.project.client.name,
        'allocation_type': allocation.allocation_type,
        'note': allocation.note
    } for allocation in Allocation.objects.all()]

    if request.user.is_authenticated():
        return JsonResponse(response, safe=False)
    else:
        return HttpResponseForbidden('You must authenticate')
