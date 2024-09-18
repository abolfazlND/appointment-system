from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('phone_number', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'is_active', 'is_staff')
