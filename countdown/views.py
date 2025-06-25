from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Birthday
from .forms import BirthdayForm

import datetime
# Create your views here.


class CountdownListView(ListView):
    model = Birthday
    template_name = 'countdown_list.html'

    def get_context_data(self, **kwargs):
        context = super(CountdownListView, self).get_context_data(**kwargs)
        nearest_birthday = None
        smallest_time_remaining = None

        for i in Birthday.objects.all():
            if (i.month > datetime.datetime.now().month) or (i.month == datetime.datetime.now().month and i.day > datetime.datetime.now().day):
                remaining_year = datetime.datetime.now().year
            else:
                remaining_year = datetime.datetime.now().year+1

            upcoming_birthday = datetime.datetime(
                remaining_year,
                i.month,
                i.day
            )
            time_remaining = upcoming_birthday - datetime.datetime.now()

            birthdays_today = Birthday.objects.filter(month=datetime.datetime.now().month).filter(day=datetime.datetime.now().day)
            if len(birthdays_today) > 0:
                context['nearest_birthdays'] = birthdays_today
                context['birthday_today'] = True
                context['header_font_size'] = str(64//len(context['nearest_birthdays']))+'px'
                break
            elif i == Birthday.objects.all()[0] or time_remaining < smallest_time_remaining:
                smallest_time_remaining = time_remaining
                nearest_birthday = i
                context['nearest_birthdays'] = Birthday.objects.filter(month=nearest_birthday.month).filter(day=nearest_birthday.day)
                context['birthday_today'] = False
                context['header_font_size'] = str(64//len(context['nearest_birthdays']))+'px'
                context['days'] = time_remaining.days
                context['hours'] = time_remaining.seconds // 3600
                context['minutes'] = (time_remaining.seconds % 3600) // 60
                context['seconds'] = time_remaining.seconds % 60
        return context


class CountdownDetailView(DetailView):
    model = Birthday
    template_name = 'countdown_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CountdownDetailView, self).get_context_data(**kwargs)
        birthday_month = self.get_object().month
        birthday_day = self.get_object().day
        if (birthday_month > datetime.datetime.now().month) or (birthday_month == datetime.datetime.now().month and birthday_day > datetime.datetime.now().day):
            remaining_year = datetime.datetime.now().year
        else:
            remaining_year = datetime.datetime.now().year+1

        upcoming_birthday = datetime.datetime(
            remaining_year,
            birthday_month,
            birthday_day
        )
        time_remaining = upcoming_birthday - datetime.datetime.now()
        if time_remaining.days == 364:
            context['birthday_today'] = True
        else:
            context['birthday_today'] = False
            context['days'] = time_remaining.days
            context['hours'] = time_remaining.seconds // 3600
            context['minutes'] = (time_remaining.seconds % 3600) // 60
            context['seconds'] = time_remaining.seconds % 60
        return context


class CountdownCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm
    template_name = 'countdown_create.html'

    def form_valid(self, form):
        form.instance.month = form.cleaned_data['date'].month
        form.instance.day = form.cleaned_data['date'].day
        return super(CountdownCreateView, self).form_valid(form)
