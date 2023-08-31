
from django.urls import path
from . import views

urlpatterns = [

    # ========== API Endpoints ==================================+++++++++++++++=======================================
    path("", views.TodoListApiView.as_view()),
    path("<int:id>/", views.todolist_detail),


]
