from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.forms import ProfileForm,MovieForm
from core.models import Profile, Movie


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profiles')
        return render(request, 'core/index.html')
    

method_decorator(login_required, name = 'dispatch')
class UploadMovie(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/video_upload.html')

    def post(self,request,*args,**kwargs):
        form = MovieForm(request.POST, request.FILES or None)
        
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            
            if form.save():
                return redirect('upload_film')
    
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
method_decorator(login_required, name = 'dispatch')
class ProfileHome(View):
    def get(self, request, profile_id, *args, **kwargs):
        
        try:
            profile = Profile.objects.get(uuid = profile_id)
            movies = Movie.objects.all()
            try:
                show_case = movies[0]
            except:
                show_case = None
            
            if profile not in request.user.profiles.all():
                return redirect(to='core:profiles')    
            
            return render(request, 'movie_list.html', {'movies':movies, 'show_case':show_case})
        except Profile.DoesNotExist:
            return redirect(to='core:profiles')
method_decorator(login_required, name = 'dispatch')
class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid = movie_id)
            return render(request, 'movie_detail.html',{'movie':movie})
        except movie.DoesNotExist:
            redirect(to='core:profileHome')
method_decorator(login_required, name = 'dispatch')
class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid = movie_id)
            
            return render(request, 'show_movie.html',{'movie':movie})
        except movie.DoesNotExist:
            redirect(to='core:profileHome')
            
            
