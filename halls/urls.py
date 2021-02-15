"""urls for the app halls."""
from django.urls import path

from halls.views import (
    CreateHall,
    DetailHall,
    UpdateHall,
    DeleteHall,
    add_video,
)

app_name = "halls"

urlpatterns = [
    path("create/", CreateHall.as_view(), name="create_hall"),
    path("detail/<int:pk>", DetailHall.as_view(), name="detail_hall"),
    path("update/<int:pk>", UpdateHall.as_view(), name="update_hall"),
    path("delete/<int:pk>", DeleteHall.as_view(), name="delete_hall"),
    # video
    path("AddVideo/<int:pk>/", add_video, name="add_video"),
]
