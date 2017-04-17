from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from lmn.api_twitter import tweet

from .models import Note


@receiver(post_save, sender=Note)
def post_to_twitter(sender, instance, created, **kwargs):
    # kwargs['instance'] is the Note object in questions
    # note = kwargs['instance']
    note = instance
    # only tweet on creation, not updates or deletions
    if created:
        # TODO would like to pass REST url of note as second parameter
        # Not sure how to get that
        tweet(note.title)  # TODO error handling


