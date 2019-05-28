from django.db import models
from django.contrib.auth.models import User


class Standard(models.Model):
    name_standard = models.CharField(max_length=120)

    def __str__(self):
        return self.name_standard


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    bio = models.TextField()
    joining_date = models.DateField(auto_created=True, null=True)

    def __str__(self):
        return ("%s %s" % (self.user.first_name, self.user.last_name)).upper()


class Subject(models.Model):
    name_subject = models.CharField(max_length=120)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='standard_subjects', null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subject_teaches', null=True)

    def __str__(self):
        return  self.name_subject + " - " + self.standard.name_standard


class Book(models.Model):
    title = models.CharField(max_length=120)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='book_subject')

    def __str__(self):
        return self.title


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=120)
    relation_to_student = models.CharField(max_length=120, default='Father')
    contact_number = models.IntegerField(null=True, default=0)

    def __str__(self):
        return ("%s %s" % (self.user.first_name, self.user.last_name)).upper()



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_students', null=True)
    admission_date = models.DateTimeField(auto_now=True, editable=True)
    roll_number = models.IntegerField(default=0)
