from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.forms import ProfileForm,MovieForm
from core.models import Profile, Movie
import requests
import json

api_key = 'c9ad551c621fd58b2a973511eb5b4306'

def get_movie_id(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={title}&page=1&include_adult=false"
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        guess_movie_id = json_data['results'][0]['id']
    return guess_movie_id

def get_movie_details(movie_id):
     
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = json.loads(response.text)
        description = json_data['overview']
        backdrop_path = json_data['backdrop_path']
        original_title = json_data['original_title']
        release_date = json_data['release_date']
        runtime = json_data['runtime']
        vote_average = json_data['vote_average']
        tagline = json_data['tagline']
        
    return description,backdrop_path,original_title,release_date,runtime,vote_average,tagline

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
        duplicate_movie = False
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            
            movie_id = get_movie_id(title)
            description,backdrop_path,original_title,release_date,runtime,vote_average,tagline = get_movie_details(movie_id)
            
            form.description = description
            form.backdrop_path = backdrop_path
            form.original_title = original_title
            form.release_date = release_date
            form.runtime = runtime
            form.vote_average = vote_average
            
            movie = Movie()
            movie.title = title
            movie.file = file
            movie.description = description
            movie.original_title = original_title
            movie.release_date = release_date
            movie.runtime = runtime
            movie.vote_average = vote_average
            movie.tagline = tagline
            
            movies = Movie.objects.all()
            
            for mov in movies:
                print(mov.original_title)
                if mov.title == movie.title:
                    duplicate_movie == True
                    return
                
            if not duplicate_movie:
                movie.save()
                
            return redirect('core:profiles')
            
                
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
            
            
