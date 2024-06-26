from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request, wallet):
    profile = Profile.objects.get(user=request.user)
    profile.wallet = wallet
    profile.set_referrals()
    profile.set_rank()
    my_recs = profile.get_recommened_profiles()
    context = {'my_recs':my_recs}
    return render(request, 'principal/profile.html', context)

def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    profile.set_referrals()
    profile.set_days()
    profile.set_rank()
    profile.set_points()
    my_recs = profile.get_recommened_profiles()
    context = {'my_recs':my_recs}
    return render(request, 'principal/profile.html', context)

def signup_view(request):
    profile_id = request.session.get('ref_profile')
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        if profile_id is not None:
            recommended_by_profile = Profile.objects.get(id=profile_id)
            instance = form.save()
            registered_user = User.objects.get(id = instance.id)
            registered_profile = Profile.objects.get(user=registered_user)
            registered_profile.recommended_by = recommended_by_profile.user
            registered_profile.save()
        else:
            form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        wallet = form.cleaned_data.get('wallet')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(f'profile/{wallet}')
    context = {'form':form}
    return render(request, 'principal/signup.html', context)

def main_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
    except:
        pass

    return render(request, 'principal/main.html', {})