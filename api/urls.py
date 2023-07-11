from django.urls import path
from .views import TaskList, TaskDetail,CotegoryView

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('category/',CotegoryView.as_view()),
    path('category/<int:pk>/',CotegoryView.as_view())

]