from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('view-homeworks/', views.view_homeworks, name='view_homeworks'),
    path('submit-homework/', views.submit_homework, name='submit_homework'),
    path('todo-list/', views.todo_list, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('update-todo/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('finish-todo/<int:todo_id>/', views.finish_todo, name='finish_todo'),
    path('video-tutorials/', views.video_tutorials, name='video_tutorials'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('logout/', views.logout_view, name='logout'),
]
