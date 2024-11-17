from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("solve_knapsack/", views.solve_knapsack, name="solve_knapsack"),
]