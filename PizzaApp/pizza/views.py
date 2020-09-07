from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

# pip install django-braces
from braces.views import SelectRelatedMixin

from . import models



class PizzaList(SelectRelatedMixin, generic.ListView):
    model = models.Pizza
    select_related = ()
