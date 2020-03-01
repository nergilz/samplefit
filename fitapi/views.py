from rest_framework import generics
from fitapi.models import Teacher, Lesson
from fitapi.serializers import TeacherSerializer, LessonSerializer


class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
