from django.utils.text import slugify


def generate_unique_slug(instance, value):
    """
    Generate a unique slug for a Django model instance.

    Parameters:
    - instance: The model instance for which the slug is being generated.
    - value: The value to be slugfied (e.g., the model's title).

    Returns:
    A unique slug string.
    """
    slug = slugify(value)
    base_slug = slug
    counter = 1
    ModelClass = instance.__class__

    # Check for duplicates
    while ModelClass.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
