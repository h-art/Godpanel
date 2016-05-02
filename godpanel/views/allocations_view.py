from datetime import datetime

from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.generic import View

from godpanel.models import Allocation


class AllocationsView(View):
    def get(self, request):
        start = request.GET.get('start')
        end = request.GET.get('end')

        if None in [start, end]:
            response = JsonResponse({'message': 'start and end parameters are required'})
            response.status_code = 400
            return response

        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')

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
        } for allocation in Allocation.objects.filter(start__gte=start_date, end__lte=end_date)]

        if request.user.is_authenticated():
            return JsonResponse(response, safe=False)
        else:
            return HttpResponseForbidden('You must authenticate')
