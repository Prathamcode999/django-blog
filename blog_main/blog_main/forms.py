from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2'] # password1 is for password and password2 is for confirm password


class loginForm():
    class Meta:
        model: User
        fields = ['username','password']