from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from lmn.models import Profile

# Register your models here, for them to be displayed in the admin view

from .models import Venue, Artist, Note, Show

admin.site.register(Venue)
admin.site.register(Artist)
admin.site.register(Note)
admin.site.register(Show)

# We do the below stuff so user profile details show up in Django admin

# https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#extending-the-existing-user-model
# Define an inline admin descriptor for Profile model which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
