from django.urls import path

from .views import UserCountView, ManageFeesView

urlpatterns = [
    path("user-count/", UserCountView.as_view()),
    path("manage-fees/", ManageFeesView.as_view()),
]
