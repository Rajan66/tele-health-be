from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from gatekeeper.models import User


# Custom form for creating users
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email", "role")

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data.get("password1"):
            user.set_password("DefaultPass123!")
        if commit:
            user.save()
        return user


# Custom form for changing users
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "role",
            "is_active",
            "is_staff",
        )


# Custom admin
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = (
        "first_name",
        "last_name",
        "email",
        "role",
        "is_staff",
        "is_active",
    )
    ordering = ("email",)
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "role")

    # Fieldsets for editing existing users
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "role",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    # Fieldsets for adding new users
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


# Register the custom admin
admin.site.register(User, UserAdmin)
