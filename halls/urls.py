from django.urls import path

from halls.views import CreateHall

app_name = 'halls'

urlpatterns = [
    path('create/', CreateHall.as_view(), name='halls_create'),
]
