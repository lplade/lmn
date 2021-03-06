from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .restrict_file import ContentTypeRestrictedFileField
from .validators import file_size, image_extensions

import datetime

# Every model gets a primary key field by default.

# Users, venues, shows, artists, notes

User._meta.get_field('email')._unique = True

# Require email, first name and last name
User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

##############################################################################


class Profile(models.Model):
    """User profile"""
    # from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=200)
    favorite_bands = models.CharField(max_length=60)
    starred_user = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({}, {}) {}'.format(
            self.user.username, self.user.last_name,
            self.user.first_name, self.description
        )

##############################################################################


class Artist(models.Model):
    """Representative of a music artist"""
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "Artist: " + self.name


class Venue(models.Model):
    """Venue object."""
    # TODO Add more information to the venue model
    name = models.CharField(max_length=200, blank=False, unique=True)
    city = models.CharField(max_length=200, blank=False)
    # What about international?
    state = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return 'Venue name: {} in {}, {}'.format(
            self.name, self.city, self.state
        )


''' A show - one artist playing at one venue at a particular date. '''


class Show(models.Model):
    show_date = models.DateTimeField(blank=False)
    artist = models.ForeignKey(Artist)
    venue = models.ForeignKey(Venue)

    def __str__(self):
        return 'Show with artist {} at {} on {}'.format(
            self.artist, self.venue, self.show_date
        )


''' One user's opinion of one show. '''


class Note(models.Model):
    show = models.ForeignKey(Show, blank=False)
    user = models.ForeignKey('auth.User', blank=False)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=1000, blank=False)
    posted_date = models.DateTimeField(blank=False)
    document = models.FileField(upload_to='images/',
                                validators=[file_size, image_extensions], blank=True)

    def publish(self):
        posted_date = datetime.datetime.today()
        self.save()

    def __str__(self):
        return 'Note for user ID {} for show ID {} with ' \
               'title {} text {} posted on {} picture {}'\
            .format(self.user, self.show, self.title,
                    self.text, self.posted_date, self.document)
