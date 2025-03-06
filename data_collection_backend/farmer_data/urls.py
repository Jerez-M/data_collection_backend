from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateFarmDataView.as_view(), name="create_farm_data"),
    path("<int:pk>/", views.FarmDataReadUpdateDestroyView.as_view()),
    path("get-all/", views.GetAllFarmDatas.as_view()),
]
