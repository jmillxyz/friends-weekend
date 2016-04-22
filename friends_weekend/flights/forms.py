from django import forms

from .models import Flight


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        fields = ('airline', 'number')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(FlightForm, self).__init__(*args, **kwargs)
