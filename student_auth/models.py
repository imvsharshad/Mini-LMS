from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='homework_images/')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubmittedHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submitted_homeworks/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.homework.title}"

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.description[:50]}"

class VideoTutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail_url = models.URLField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    query = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.roll_number}"
