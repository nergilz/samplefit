from django.urls import path
from fitapi.views import TeacherList, LessonList


urlpatterns = [
    path('teachers/', TeacherList.as_view()),
    path('lessons/', LessonList.as_view())
    ]
