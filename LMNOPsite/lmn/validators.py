# From https://stackoverflow.com/a/35321718

from django.core.exceptions import ValidationError


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


# then in your form with the File field you have something like this
# image = forms.FileField(required=False, validators=[file_size])


# https://stackoverflow.com/a/27081099

def image_extensions(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.gif', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
