from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View


class FrontView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'index.html', {})
        else:
            return redirect('%s%s' % (reverse('admin:login'), '?next=%s' % (reverse('godpanel.frontpage'))))
