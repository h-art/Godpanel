from django.conf.urls import url

from godpanel.views.allocations_view import AllocationsView
from godpanel.views.employees_view import EmployeesView
from godpanel.views.front_view import FrontView

urlpatterns = [
    url(r'^$', FrontView.as_view(), name='godpanel.frontpage'),
    url(r'^employees/', EmployeesView.as_view(), name='godpanel.employees'),
    url(r'^allocations/', AllocationsView.as_view(), name='godpanel.allocations'),
]
