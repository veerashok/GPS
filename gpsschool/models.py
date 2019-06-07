from django.db import models
from django.contrib.auth.models import User
from .constants import ( SEX_CHOICES, ETHNICITY_CHOICES, COUNTRY_CHOICES,
        PAYMENT_SCHEDULES, SCHOLARSHIP_CHOICES, TASK_TYPE)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import datetime
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import ugettext as _


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcement-detail', kwargs={'pk': self.pk})


class Location(models.Model):
    address1    = models.CharField(max_length=200)
    address2    = models.CharField(max_length=200)
    address3    = models.CharField(max_length=200)
    city        = models.CharField(max_length=200)
    state       = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    country     = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

    def __str__(self):
        answer = self.address1 + '\n'

        if self.address2 != None:
            answer += self.address2 + '\n'
        if self.address3 != None:
            answer += self.address3 + '\n'

        answer += self.city + ', ' + self.state + ', ' + self.postal_code + ', ' + self.country

        return answer


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.IntegerField()
    bio = models.TextField()
    joining_date = models.DateField(auto_created=True, null=True)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact_number = models.IntegerField(null=True)

    def __str__(self):
        return ("%s %s" % (self.user.first_name, self.user.last_name)).upper()


class Standard(models.Model):
    name_standard = models.CharField(max_length=120)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_standard

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

class Payments(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    comment = models.TextField(null=True)

    def __str__(self):
        return str(self.date) + ' - ' + str(self.amount)


class PaymentSchedule(models.Model):
    yearly_cost = models.FloatField(default=0)
    payment_schedule = models.CharField(max_length=2, choices=PAYMENT_SCHEDULES)
    scholarship_type = models.CharField(max_length=2, choices=SCHOLARSHIP_CHOICES, default=None)
    scholarship_amount = models.FloatField(default=0)
    transactions = models.ManyToManyField(Payments, related_name='user_transactions')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    father_name = models.CharField(null=True, max_length=120)
    mother_name = models.CharField(null=True, max_length=120)
    contact_number = models.CharField(null=True, max_length=120)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    admission_date = models.DateTimeField(auto_now=True, editable=True)
    roll_number = models.IntegerField(default=0)
    year = models.IntegerField(_('year'), validators=[MinValueValidator(1984), max_value_current_year], null=True)
    account = models.OneToOneField(PaymentSchedule, on_delete=models.CASCADE)

    class Meta:
        ordering = ['roll_number']

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Task(models.Model):
    task_type = models.CharField(max_length=2, choices=TASK_TYPE)
    date_assigned = models.DateTimeField(blank=True)
    date_completed = models.DateTimeField(blank=True)
    score = models.FloatField(default=0)
    maximum_score = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        i = 0
        for x in TASK_TYPE:
            if x[0] == self.task_type:
                break
            i += 1

        return TASK_TYPE[i][1] + '-' + self.standard.name_standard
