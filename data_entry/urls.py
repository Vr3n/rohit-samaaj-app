from django.urls import path
from . import views

urlpatterns = [
    path("data-entry/", views.DataEntryFormView.as_view(), name="data-entry-form"),
]
