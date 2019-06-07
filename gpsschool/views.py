from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import (
    Announcement, Teacher,
    Standard, Student,
    PaymentSchedule
)


def home(request):
    context = {
        'posts': Announcement.objects.all()
    }
    return render(request, 'gpsschool/home.html', context)

class PaymentScheduleListView(LoginRequiredMixin, ListView):
    model = PaymentSchedule
    context_object_name = 'payments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fees_deposited'] = 1000
        return context

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'


class StandardListView(LoginRequiredMixin, ListView):
    model = Standard
    context_object_name = 'standards'

class StandardDetailView(LoginRequiredMixin, DetailView):
    model = Standard
    context_object_name = 'standard'

class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    context_object_name = 'teachers'
    ordering = ['joining_date']
    paginate_by = 5

class AnnouncementListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'gpsschool/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    ordering = ['-date_posted']
    paginate_by = 5


class UserAnnouncementListView(ListView):
    model = Announcement
    template_name = 'gpsschool/user_announcements.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'announcements'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Announcement.objects.filter(author=user).order_by('-date_posted')


class AnnouncementDetailView(DetailView):
    model = Announcement


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False


class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = '/dashboard/'

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False


def about(request):
    return render(request, 'gpsschool/about.html', {'title': 'About'})
