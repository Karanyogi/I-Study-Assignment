from django.urls import path
from . import views

app_name='pizza'

urlpatterns = [
    path('', views.PizzaList.as_view(), name="PizzaList"),
]
