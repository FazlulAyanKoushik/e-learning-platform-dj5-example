from django.shortcuts import render
from django.views.generic.list import ListView
from courses.models import Course
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.
class ManageCourseListView(ListView):
    model = Course
    template_name = "courses/manage/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
