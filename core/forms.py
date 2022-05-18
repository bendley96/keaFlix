from django.forms import ModelForm
from core.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=['uuid']