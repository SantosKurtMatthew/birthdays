from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone

from .models import Birthday
from .forms import BirthdayForm


# Create your views here.
class CountdownListView(ListView):
    model = Birthday
    template_name = 'countdown_list.html'

class CountdownDetailView(DetailView):
	model = Birthday
	template_name = 'countdown_detail.html'

	def get_context_data(self, **kwargs):
		context = super(CountdownDetailView, self).get_context_data(**kwargs)
		time_remaining = self.get_object().date - timezone.now()
		print(time_remaining)

		return context

class CountdownCreateView(CreateView):
	model = Birthday
	form_class = BirthdayForm
	template_name = 'countdown_create.html'