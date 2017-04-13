from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import lmn.social_twitter

from .models import Note

@receiver(post_save, sender=Note)
def post_to_twitter(sender, instance, created, **kwargs):
    # kwargs['instance'] is the Note object in questions
    note = kwargs['instance']
    if created:
        # TODO do stuff with twitter

