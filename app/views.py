# -*- coding: utf-8 -*-
from django.views.generic import View, ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Person
from app.forms import PersonForm
from django.shortcuts import render
from django.http import JsonResponse

class Index(TemplateView):
    """
    Class that shows the start template.
    """
    template_name = "app/index.html"


class List(ListView):
    """
    Class that lists the Person objects.
    """
    model = Person
    template_name = 'app/person_list.html'
    context_object_name = 'people'


class Create(View):
    def  get(self, request):
        first_name1 = request.GET.get('first_name', None)
        last_name1 = request.GET.get('last_name', None)

        obj = Person.objects.create(
            first_name = first_name1,
            last_name = last_name1,
        )

        person = {'id':obj.id,'first_name':obj.first_name,'last_name':obj.last_name}

        data = {
            'person': person
        }
        return JsonResponse(data)


class Update(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        first_name1 = request.GET.get('first_name', None)
        last_name1 = request.GET.get('last_name', None)

        obj = Person.objects.get(id=id1)
        obj.first_name = first_name1
        obj.last_name = last_name1
        obj.save()

        person = {'id':obj.id,'first_name':obj.first_name,'last_name':obj.last_name}

        data = {
            'person': person
        }
        return JsonResponse(data)


class Delete(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Person.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class Detail(View):
    """
    Class that allows you to see the details of a Person object
    """
    model = Person
    template_name = 'app/person_detail.html'

# Create your views here.
