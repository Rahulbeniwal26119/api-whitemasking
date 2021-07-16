from  django.urls import path, include
from .views import DullView, GetAnotherApiData
urlpatterns = [
    path("dullapi/", DullView.as_view(), name="dullapi"),
    path("externalapi/", GetAnotherApiData.as_view(), name="externalapi")
    ]