from django.contrib import admin
from .models import Homework, SubmittedHomework, TodoItem, VideoTutorial, ContactSubmission

admin.site.register(Homework)
admin.site.register(SubmittedHomework)
admin.site.register(TodoItem)
admin.site.register(VideoTutorial)
admin.site.register(ContactSubmission)