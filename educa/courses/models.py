from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel
from common.utils import generate_unique_slug

User = get_user_model()


# Create your models here.
class Subject(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Call the helper function to generate a unique slug
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)


class Course(BaseModel):
    owner = models.ForeignKey(
        User,
        related_name='courses_created',
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Call the helper function to generate a unique slug
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)


class Module(BaseModel):
    course = models.ForeignKey(
        Course, related_name='modules', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            # Call the helper function to generate a unique slug
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)
