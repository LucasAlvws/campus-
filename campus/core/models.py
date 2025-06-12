from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    COURSES = [
        ('CS', 'Computer Science'),
        ('IS', 'Information Systems'),
        ('CE', 'Computer Engineering'),
    ]
    course = models.CharField(max_length=50, choices=COURSES, blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=[('student', 'Student'), ('coordinator', 'Coordinator'), ('dce', 'Student Union')],
        default='student'
    )

class Document(models.Model):
    TYPES = [
        ('transcript', 'Academic Transcript'),
        ('enrollment', 'Enrollment Certificate'),
        ('syllabus', 'Course Syllabus'),
    ]
    doc_type = models.CharField(max_length=50, choices=TYPES)
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)
    estimated_date = models.DateField()
    requester = models.ForeignKey(User, on_delete=models.CASCADE)

class AcademicInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    term = models.CharField(max_length=10)
