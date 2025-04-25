from django import forms
from .models import TodoItem, ContactSubmission

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['description', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'roll_number', 'department', 'query']
        widgets = {
            'query': forms.Textarea(attrs={'rows': 4}),
        }

