from django.conf.urls import url
from godpanel import views


urlpatterns = [
    url(r'^$', views.index, name='godpanel.frontpage'),
    url(r'^employees/', views.employees, name='godpanel.employees'),
    url(r'^allocations/', views.allocations, name='godpanel.allocations'),
]
