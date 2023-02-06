from django.contrib.auth.forms import SetPasswordForm
from .models import User

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']