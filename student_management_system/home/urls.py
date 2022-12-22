from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.index),
    path('login', views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('formdata',views.formdata, name='formdata'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('course', views.course, name='course'),
    path('add_course',views.add_course, name='add_course'),
    path("update_course",views.update_course, name='update_course'),
    path("delete_course",views.delete_course, name='delete_course'),
    path('students', views.student, name='student'),
    path('add_student',views.add_student, name='add_student'),
    path("update_student",views.update_student, name='update_student'),
    path("delete_student",views.delete_student, name='delete_student'),
    path('teacher', views.teacher, name='teacher'),
    path('add_teacher',views.add_teacher, name='add_teacher'),
    path("update_teacher",views.update_teacher, name='update_teacher'),
    path("delete_teacher",views.delete_teacher, name='delete_teacher'),
    path("update_teacher_page/<int:uid>/",views.update_teacher_page, name='update_teacher_page'),
    path("update_student_page/<int:uid>/",views.update_student_page, name='update_teacher_page'),
    path("update_course_page/<int:uid>/",views.update_course_page, name='update_teacher_page'),
    path("search_student",views.search_student, name='search_student'),
    path("search_course",views.search_course, name='search_course'),
    path("search_teacher",views.search_teacher, name='search_teacher'),

]