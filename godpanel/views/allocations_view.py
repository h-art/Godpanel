import json
from datetime import datetime

from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.generic import View

from godpanel.models import Allocation
from godpanel.views.allocations_form_view import AllocationForm


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
                                        hour=23,
                                        minute=59),
                        'saturation': allocation.saturation,
                        'title': allocation.project.name,
                        'client': allocation.project.client.name,
                        'allocation_type': allocation.allocation_type,
                        'note': allocation.note
                    } for allocation in Allocation.objects.filter(end__gte=start_date, start__lte=end_date)]

        if request.user.is_authenticated():
            return JsonResponse(response, safe=False)
        else:
            return HttpResponseForbidden('You must authenticate')

    def post(self, request):
        request_object = json.loads(request.body.decode('utf-8'))
        form = AllocationForm(request_object)

        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'ciao'})
        else:
            return JsonResponse(dict(form.errors), status=400)

    def put(self, request):
        request_object = json.loads(request.body.decode('utf-8'))
        allocation = Allocation.objects.get(pk=request_object['id'])

        # for error-checking, we use model form
        form = AllocationForm(request_object, instance=allocation)

        if not form.is_valid():
            # return JSON response with errors
            return JsonResponse(dict(form.errors), status=400)

        try:
            allocation.save(force_update=True)
            response = JsonResponse({'message': 'resource %d updated' % (int(request_object['id']))})
        except Exception as e:
            response = JsonResponse({
                'message': 'error updating resource with id %d' % (int(request_object['id'])),
                'stack_trace': str(e)
            }, status=500)

        return response
