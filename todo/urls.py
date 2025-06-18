from django.urls import path
from . import views
urlpatterns=[
    path('addTask', views.addTask, name='addTask'),
    #mark as done
    path('updateTask/<int:pk>', views.updateTask, name='updateTask'),
    #mark as undone
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
    #edit task
    path('edit/<int:pk>', views.edit, name='edit'),
    # delete task
    path('delete/<int:pk>', views.delete, name='delete'),

]