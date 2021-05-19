from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username': {
                'required': 'Name is required'
            },
            'email': {
                'required': 'Email is required'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.is_active = True
            user.save()
        return user
