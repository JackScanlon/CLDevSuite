from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserAccountCreationForm, UserAccountChangeForm
from .models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = UserAccount
    list_display = [
        'email',
        'username',
    ]
