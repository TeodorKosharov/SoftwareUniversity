from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from cbv.web.models import Employee
from django import forms


# reverse vs reverse_lazy
# success_url = reverse_lazy('urlname') - това означава, че когато ни потрябва този url тогава ще го получим
# success_url = reverse('urlname') - веднага ни дава този url


class IndexView(views.View):
    def get(self, request):  # if the request.method == 'GET'
        # self.kwargs - това са нещата, които са подадени в url-а

        context = {
            'title': 'CBV Demo'
        }

        return render(request, 'index.html', context)


class IndexView2(TemplateView):
    # Даваме име на темплейта, който искаме да рендерираме
    template_name = 'index.html'

    # static context - Данните тук са статични и при извикване на view-то няма актуализация на данните
    extra_context = {
        'title': 'Template CBV Demo'
    }

    # dynamic context - При всяко извикване на view-то информацията от динамичния контекс ще се актуализирва
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context

    # Методът get_context_data, който override-ваме проверява дали имаме подадени стойности в extra_context-а
    # и ако има такива ги добавя към context-а


class IndexViewWithListView(ListView):
    # Това view показва списък от Employee-та, защото това е модела, който сме подали

    context_object_name = 'employees'  # Това е името на променливата, която обхождаме в темплейта. По default
    # тя се казва object_list, но понеже в темплейта сме записали
    # {% for employee in employees %} затова задаваме име чрез context_object_name

    model = Employee  # Това ни замества get_context_data. Този ред автоматично извиква objects.all() на посочения модел
    template_name = 'index.html'
    extra_context = {'title': 'ListView Demo'}

    # ordering
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.order_by('first_name')
    #     return queryset

    # filtering
    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.request.GET.get('pattern', None)
        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern.lower())
        return queryset


class EmployeeDetailsView(DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'details.html'


# Form:
class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'first_name': 'First Name'
        }


class EmployeeCreateView(CreateView):
    template_name = 'create.html'
    model = Employee
    fields = '__all__'
    success_url = '/'

    # form_class = EmployeeCreateForm

    def get_form_class(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for name, field in form.fields.items():
            field.widget.attrs['placeholder'] = 'Enter' + name

        return form

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={'pk': created_object.pk})


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'edit.html'

    def get_success_url(self):
        created_object = self.object
        return reverse('employee details', kwargs={'pk': created_object.pk})
