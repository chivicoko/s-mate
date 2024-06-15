from django.urls import path
from .views import home, teacher, new_question, add_test, student, student_past_questions, student_subjects, blog, post_detail, success, new_blog_post, register_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/new_question/', new_question, name='new_question'),
    path('teacher/add_test/', add_test, name='add_test'),
    path('student/', student, name='student'),
    path('student/student_past_questions', student_past_questions, name='student_past_questions'),
    path('student/student_subjects', student_subjects, name='student_subjects'),
    path('blog/', blog, name='blog'),
    path('blog/new_blog_post/', new_blog_post, name='new_blog_post'),
    path('success/', success, name='success'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]