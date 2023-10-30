from .views import create_customer, view_customer
from django.urls import path

urlpatterns = [
    path("create_customer", create_customer, name="home page"),
    path("view_customer", view_customer, name="get page"),
]
