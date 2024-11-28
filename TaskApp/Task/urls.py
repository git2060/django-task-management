from django.urls import path
from . import views

urlpatterns=[
    path("", views.view_task, name="view_task"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
     path("update/<int:pk>/", views.update_task, name="update_task")
]