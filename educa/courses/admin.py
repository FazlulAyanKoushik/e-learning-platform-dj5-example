from django import forms
from django.contrib import admin

from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


# Custom form for Module Inline to include prepopulated_fields
class ModuleInlineForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'
        # Specify the prepopulated fields mapping
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'vTextField'}),
        }

    class Media:
        # Include the necessary JS for the slug population
        js = ('admin/js/prepopulate.js',)


class ModuleInline(admin.StackedInline):
    model = Module
    form = ModuleInlineForm
    prepopulated_fields = {'slug': ('title',)}  # Add the prepopulated fields here


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created_at']
    list_filter = ['created_at', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
