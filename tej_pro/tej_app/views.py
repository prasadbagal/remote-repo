from tej_app import forms
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from tej_app.models import MyModel
from django_datatables_view.base_datatable_view import BaseDatatableView

# Create your views here.


def index(request):
    return render(request, "tej_app/index.html")


def formpage(request):
    form = forms.FormName()
    return render(request, "tej_app/forms.html", {"form": form})


class MyModellListJson(BaseDatatableView):
    model = MyModel

class TestModelList(TemplateView):
    template_name = 'tej_app/mymodel_list.html'


class ArticleDetailView(ListView):
    model = MyModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [field.name for field in MyModel._meta.get_fields()]
        return context
