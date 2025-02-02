from django.urls import path
from .views import get_tasks, create_task, task_detail, task_done, updateOrder

urlpatterns = [
    path("tasks/", get_tasks, name="get_tasks"),
    path("tasks/create", create_task, name="create_task"),
    path("tasks/<int:pk>", task_detail, name="task_detail"),
    path("done/<int:pk>", task_done, name="task_done"),
    path("update/", updateOrder, name="updateOrder")
]
