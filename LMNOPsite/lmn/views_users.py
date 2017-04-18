from .models import Venue, Artist, Note, Show, Profile
from .forms import VenueSearchForm, NewNoteForm, ArtistSearchForm, \
    UserRegistrationForm, UserModificationForm, UserProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render, redirect

from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone


def user_profile(request, user_pk):

    user = User.objects.get(pk=user_pk)
    usernotes = Note.objects.filter(
        user=user.pk).order_by('posted_date').reverse()

    return render(request, 'lmn/users/user_profile.html',
                  {'user': user, 'notes': usernotes})


@login_required
def my_user_profile(request):

    try:

        profile = Profile.objects.get(user=request.user.id)

    except ObjectDoesNotExist:

        profile = None

    if request.method == 'POST':

        form = UserProfileForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            profile.description = data['description']
            profile.favorite_bands = data['favorite_bands']
            profile.save()

        return render(request, 'lmn/users/modify_user.html',
                      {'form': form, 'profile': profile})

    else:

        form = UserProfileForm()

    return render(request, 'lmn/users/modify_user.html',
                  {'form': form, 'profile': profile})


@login_required
def modify_user(request):
    """
    User modification view
    GET: render UserModificationForm (/LMNOPsite/lmn/views.py)
    POST: query lmnop DB for user by pk, update user with information from
        form.
    """
    if request.method == 'POST':
        form = UserModificationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(pk=request.user.id)
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.password = data['password1']
            user.save()

            return redirect('lmn:homepage')

        else:
            return render(request, 'lmn/users/change_password.html',
                          {'form': form})
    else:
        form = UserModificationForm()
        return render(request, 'lmn/users/change_password.html',
                      {'form': form})


def register(request):
    """
    Allows users to register profiles using built-in Django model auth.user
    """
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1'])
            login(request, user)
            return redirect('lmn:homepage')

        else:
            message = 'Please check the data you entered'
            return render(request, 'registration/register.html',
                          {'form': form, 'message': message})

    else:
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})


def logout_message(request):
    """Logout redirect"""
    return render(request, 'lmn/users/logout_message.html')
