from django import forms
from categories.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'order')

        labels = {
            'name': 'Category Name',
            'description': 'Description',
            'order': 'Display Order',
        }

        error_messages = {
            'name': {
                'required': 'Category name is required.',
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError(
                'Category name must be at least 3 characters long.'
            )
        return name