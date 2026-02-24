from django import forms
from .models import Tutorial
class TutorialCreateForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        exclude = ('is_published', 'created_at')
        labels = {
            'title': 'Tutorial Title',
            'summary': 'Short Description',
            'content': 'Tutorial Content',
            'difficulty': 'Difficulty Level',
            'estimated_time': 'Estimated Time (minutes)',
            'categories': 'Category',
            'techniques': 'Techniques Used',
        }

        error_messages = {
            'title': {
                'required': 'A tutorial title is required.',
            },
            'summary': {
                'required': 'Please provide a short summary.',
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError(
                'Title must be at least 5 characters long.'
            )
        return title

    def clean_estimated_time(self):
        time = self.cleaned_data.get('estimated_time')
        if time <= 0:
            raise forms.ValidationError(
                'Estimated time must be greater than zero.'
            )
        return time

    
class TutorialEditForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = '__all__'

        labels = {
            'created_at': 'Created On',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['created_at'].disabled = True
