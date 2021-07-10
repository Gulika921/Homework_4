from django.urls import path, include
from car.views import CarListView, CarDetailView, CarCreateView, CarModelCreateView, CarDetailView, CarModelListView
urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/create", CarCreateView.as_view(), name="car-create"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("carmodel/", CarModelListView.as_view(), name="car_model-list"),
    path("carmodel/create", CarModelCreateView.as_view(), name="car_model-create"),
    path("carmodel/<int:pk>", CarModelListView.as_view(), name="car_model-detail"),
]
