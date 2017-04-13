# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-04-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import lmn.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0004_note_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='document',
            field=models.FileField(upload_to='images/', validators=[lmn.validators.file_size, lmn.validators.image_extensions]),
        ),
    ]
