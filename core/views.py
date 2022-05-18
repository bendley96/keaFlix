from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.forms import ProfileForm
from core.models import Profile

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profiles')
        return render(request, 'core/index.html')
    
    
method_decorator(login_required, name = 'dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, 'profile_list.html', { 'profiles':profiles })
    
    
method_decorator(login_required, name = 'dispatch')
class CreateProfile(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'profile_create.html', {'form':form})
    
    def post(self,request,*args,**kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            #print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profiles')
        return render(request, 'profile_create.html', {'form':form})