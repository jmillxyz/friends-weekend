from django.conf.urls import url

from . import views


urlpatterns = [

    url(regex=r'^$',
        view=views.FlightListView.as_view(),
        name='list'),

    url(regex=r'^add/$',
        view=views.FlightCreateView.as_view(),
        name='add'),

    url(regex=r'^(?P<number>[\w-]+)/$',
        view=views.FlightDetailView.as_view(),
        name='detail'),
]
