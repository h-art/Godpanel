from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.generic import View

from godpanel.models import Employee


class EmployeesView(View):
    def get(request):
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
