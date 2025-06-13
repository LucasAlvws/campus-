from django.contrib.auth.models import AbstractUser
from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

class User(AbstractUser):
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
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
