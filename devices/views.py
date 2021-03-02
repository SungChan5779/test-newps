from django.views.generic import ListView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from . import models, mixins



# Create your views here.

def HomeView(request):
    filter_args={}
    filter_args["host"] = request.user.pk
    filter_args["device_select"] = "ups"
    ups = models.Device.objects.filter(**filter_args).order_by('name')
    filter_args["device_select"] = "th"
    th = models.Device.objects.filter(**filter_args)
    filter_args["device_select"] = "con"
    con = models.Device.objects.filter(**filter_args)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["ups"] = models.Ups.objects.all()
    #     return context

    #print(devices)
    return render(request, "devices/device_list.html", {"ups": ups, "th": th, "con": con})
    


def Ups_detail(request, pk):
    device = models.Device.objects.get(pk=pk)
    print(dir(device.phones))

    if request.user != device.host:
        return redirect('core:home')
        
    
    device_s = device.device_select
    device_detail = device.upss.first()

    return render(request, "devices/detail_list.html", {"device": device, "device_s": device_s, "detail": device_detail})

def Th_detail(request, pk):
    device = models.Device.objects.get(pk=pk)

    if request.user != device.host:
        return redirect('core:home')

    device_s = device.device_select
    device_detail = device.temps.first()

    return render(request, "devices/detail_list.html", {"device": device, "device_s": device_s, "detail": device_detail})


def Con_detail(request, pk):
    device = models.Device.objects.get(pk=pk)

    if request.user != device.host:
        return redirect('core:home')

    device_s = device.device_select
    device_detail = device.contacts.first()

    return render(request, "devices/detail_list.html", {"device": device, "device_s": device_s, "detail": device_detail})


def Search(request):#차후수정
    print(request.GET)
    
    device = request.GET.get("device")
    filter_args = {}
    filter_args['name__contains'] = device
    filter_args["host"] = request.user.pk
    filter_args["device_select"] = "ups"
    ups = models.Device.objects.filter(**filter_args).order_by('name')
    filter_args["device_select"] = "th"
    th = models.Device.objects.filter(**filter_args)
    filter_args["device_select"] = "con"
    con = models.Device.objects.filter(**filter_args)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["ups"] = models.Ups.objects.all()
    #     return context

    #print(devices)
    return render(request, "devices/search.html", {"ups": ups, "th": th, "con": con})


def Ups(request):
    filter_args={}
    filter_args["host"] = request.user.pk
    filter_args["device_select"] = "ups"
    ups = models.Device.objects.filter(**filter_args)

    return render(request, "devices/list/ups_list.html", {"ups": ups})


def Th(request):
    filter_args={}
    filter_args["host"] = request.user.pk
    filter_args["device_select"] = "th"
    th = models.Device.objects.filter(**filter_args)

    return render(request, "devices/list/th_list.html", {"th": th})


def Con(request):
    filter_args={}
    filter_args["host"] = request.user.pk
    filter_args["device_select"] = "con"
    con = models.Device.objects.filter(**filter_args)

    return render(request, "devices/list/conn_list.html", {"con": con})


def Phone(request, pk):
    filter_args={}
    device = models.Device.objects.get(pk=pk)
    phones = device.phones
    print(phones)
    return render(request, "devices/phone_number.html", {"phones": phones})
    
    #print(phone_num)

class PhoneUpdateView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):
    model = models.Phone_Number
    
    template_name = "devices/phone_number.html"
    success_message = 'Updated'
    
    #success_url = reverse_lazy('core:home')
    
    fields = [
        "name_1",
        "phone_1",
        "name_2",
        "phone_2",
        "name_3",
        "phone_3",
        "name_4",
        "phone_4",
        "name_5",
        "phone_5",
        "name_6",
        "phone_6",
        "name_7",
        "phone_7",
        "name_8",
        "phone_8",
        "name_9",
        "phone_9",
        "name_10",
        "phone_10",
    ]
    

    def get_success_url(self):
        return reverse_lazy('devices:phoneupdate', kwargs={'pk': self.kwargs['pk']})
    
    def get_object(self, queryset=None):
        return get_object_or_404(models.Phone_Number, pk=self.kwargs['pk'])  
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name_1"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_2"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_3"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_4"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_5"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_6"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_7"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_8"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_9"].widget.attrs = {"placeholder": "이름"}
        form.fields["name_10"].widget.attrs = {"placeholder": "이름"}

        form.fields["phone_1"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_2"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_3"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_4"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_5"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_6"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_7"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_8"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_9"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        form.fields["phone_10"].widget.attrs = {"placeholder": "연락처", "type": "password",}
        
        return form
    # def get_form(self, form_class=None):
    # """Return an instance of the form to be used in this view."""
    # form = super().get_form(form_class= form_class)
    # form.fields['name_1'].widget.atts = {"value":}