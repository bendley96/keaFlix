from django.forms import ModelForm
from core.models import Profile,Movie

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=['uuid']
class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=['title', 'file']
