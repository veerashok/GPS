from django.contrib import admin
from .models import (Book, Standard, Subject,
                     Teacher, Student, Location,
                     Announcement, Task, Payments, PaymentSchedule)


def full_name(obj):
    return ("%s %s" % (obj.user.first_name, obj.user.last_name)).upper()


full_name.short_description = 'Name'

def class_strength(obj):
    f = Standard.objects.get(name_standard=obj.name_standard)
    return f.student_set.all().count()



class StudentAdmin(admin.ModelAdmin):

    list_display = (full_name, 'roll_number', 'standard', 'admission_date')
    date_hierarchy = 'admission_date'

    search_fields = ['user__first_name', 'user__last_name', 'roll_number']


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = (full_name, 'salary',)
    date_hierarchy = 'joining_date'
    list_editable = ('salary', )
    search_fields = ['user__first_name', 'user__last_name']


admin.site.register(Teacher, TeacherAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name_subject', 'standard', 'teacher')
    raw_id_fields = ('standard', 'teacher')


class StandardAdmin(admin.ModelAdmin):
    list_display = ('name_standard', class_strength, 'class_teacher')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_type', 'date_assigned', 'date_completed', 'score', 'weight', 'standard')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date')


class PaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ('yearly_cost', 'payment_schedule', 'scholarship_type', 'scholarship_amount')



admin.site.register(Book)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(Location)
admin.site.register(Announcement)
admin.site.register(Task, TaskAdmin)
admin.site.register(Payments, PaymentAdmin)
admin.site.register(PaymentSchedule, PaymentScheduleAdmin)
