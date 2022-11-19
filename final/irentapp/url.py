from django.urls import path
from . import views

app_name = "irentapp"

urlpatterns = [
    path("items/add/", views.add_items, name="add_items"),
    path("items/list/", views.list_items, name="list_items"),
    path("items/detail/<item_id>/", views.list_items, name="items_detail"),
    path("items/update/<item_id>/", views.update_items, name="update_items"),
    path("items/delete/<item_id>/", views.delete_items, name="delete_items"),

    path("items/<items_id>/question/new/", views.add_question, name="add_question")
]