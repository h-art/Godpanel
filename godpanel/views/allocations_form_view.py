import datetime as dt

from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic import View
import datetime

from godpanel.models import Allocation, Project, Employee


class AllocationForm(ModelForm):
    class Meta:
        fields = ['start', 'end', 'employee', 'project', 'saturation', 'note', 'allocation_type']
        labels = {
            'start': 'Inizio',
            'end': 'Fine',
            'employee': 'Risorsa',
            'project': 'Progetto',
            'saturation': 'Saturazione',
            'note': 'Note',
            'allocation_type': 'Tipo di allocazione',
        }
        widgets = {
            'start': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'end': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'saturation': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
            'allocation_type': forms.Select(attrs={'class': 'form-control'}),
        }
        model = Allocation


class AllocationsFormView(View):
    def get(self, request):
        method = 'put'

        if 'allocation' in request.GET:
            allocation = Allocation.objects.get(pk=request.GET['allocation'])
            form = AllocationForm(instance=allocation)
        elif 'new_allocation' in request.GET:
            form = AllocationForm(initial={
                'start': datetime.datetime.today(),
                'end': datetime.datetime.today() + dt.timedelta(days=1),
                'project': Project.objects.first().id,
                'employee': Employee.objects.get(pk=int(request.GET['resource_id'])),
                'saturation': 100
            })
            method = 'post'
        else:
            form = AllocationForm()

        return render(request, 'form/allocation.html', {'form': form, 'method': method})
