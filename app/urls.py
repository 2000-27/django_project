from .views import CustomerAPI
from django.urls import path

urlpatterns = [
    path("customer_api", CustomerAPI.as_view()),
    path("customer_api/<customer_id>", CustomerAPI.as_view()),
]
