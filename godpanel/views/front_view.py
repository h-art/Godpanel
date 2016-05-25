from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View

from godpanel.models import ClosingDay


class FrontView(View):
    def get(self, request):
        if request.user.is_authenticated():
            closing_days = ClosingDay.objects.all()
            return render(request, 'index.html', {'closing_days': closing_days})
        else:
            return redirect('%s%s' % (reverse('admin:login'), '?next=%s' % (reverse('godpanel.frontpage'))))
