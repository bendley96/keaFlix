from django.forms import ModelForm
from core.models import Profile,Movie

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=['uuid']
class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['title', 'file','original_title', 'description','backdrop_path', 'release_date','runtime', 'vote_average']
