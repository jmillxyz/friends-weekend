from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy

from braces.views import LoginRequiredMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Flight
from .serializers import FlightSerializer
from .forms import FlightForm


class FlightCreateView(LoginRequiredMixin, CreateView):
    model = Flight
    form_class = FlightForm
    success_url = reverse_lazy('flights:list')

    def get_form_kwargs(self):
        kwargs = super(FlightCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class FlightUpdateView(LoginRequiredMixin, UpdateView):
    model = Flight
    form_class = FlightForm
    success_url = reverse_lazy('flights:list')

    def get_form_kwargs(self):
        kwargs = super(FlightUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class FlightDetailView(LoginRequiredMixin, DetailView):
    model = Flight
    template_name = '../templates/flights/flight_detail.html'


class FlightListView(ListView):
    model = Flight
    template_name = '../templates/flights/flight_list.html'


class FlightListCreateAPIView(LoginRequiredMixin, ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'number'


class FlightReadUpdateDeleteView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'number'
