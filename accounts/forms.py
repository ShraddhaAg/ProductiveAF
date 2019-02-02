from django.forms import ModelForm, TextInput
from .models import Profile

class AddProfile(ModelForm):
    model = Profile
    fields = ['name','email_id', 'notification_time', 'intrests']
