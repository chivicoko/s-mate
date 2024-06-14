from django.urls import path
from .views import home, teacher, teacher_add_question, teacher_add_test, student, student_past_questions, student_subjects, blog, post_detail, success, post_blog, register_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/teacher_add_question/', teacher_add_question, name='teacher_add_question'),
    path('teacher/teacher_add_test/', teacher_add_test, name='teacher_add_test'),
    path('student/', student, name='student'),
    path('student/student_past_questions', student_past_questions, name='student_past_questions'),
    path('student/student_subjects', student_subjects, name='student_subjects'),
    path('blog/', blog, name='blog'),
    path('blog/new_post/', post_blog, name='post_blog'),
    path('success/', success, name='success'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]