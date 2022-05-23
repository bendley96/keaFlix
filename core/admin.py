from django.contrib import admin
from core.models import Movie,Profile,CustomUser,Genres

admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Genres)