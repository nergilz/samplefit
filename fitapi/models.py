from django.db import models


class Teacher(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
    availability = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name =  models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    place = models.CharField(max_length=50)
    teacher = models.CharField(max_length=100)
    startTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)
    weekDay = models.PositiveSmallIntegerField()
    appointment_id = models.CharField(max_length=200)
    service_id = models.CharField(max_length=200)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ManyToManyField(Teacher, related_name='related_teacher')

    def __str__(self):
        return self.name
