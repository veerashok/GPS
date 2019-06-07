from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    UserAnnouncementListView,
    TeacherListView,
    StandardListView,
    StandardDetailView,
    StudentListView,
    StudentDetailView,
    PaymentScheduleListView
)
from . import views


urlpatterns = [
    path('', AnnouncementListView.as_view(), name='gpsschool-home'),
    path('payments/', PaymentScheduleListView.as_view(), name='payments'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/', StudentListView.as_view(), name='students'),
    path('standards/', StandardListView.as_view(), name='standards'),
    path('standards/<int:pk>/', StandardDetailView.as_view(), name='standard-detail'),
    path('user/<str:username>', UserAnnouncementListView.as_view(), name='user-announcements'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcement/new/', AnnouncementCreateView.as_view(), name='announcement-create'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='announcement-delete'),
    path('about/', views.about, name='gpsschool-about'),
    path('faculties/', TeacherListView.as_view(), name='faculty'),
]
