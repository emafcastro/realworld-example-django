from django import forms
from django.contrib.auth import get_user_model, password_validation
from .countries import CountryField, COUNTRIES

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ["email", "name"]

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SettingsForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = User
        fields = ["email", "name", "bio", "image"]

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ContactForm(forms.Form):
    FRUIT_CHOICES = [
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
        ('mango', 'Mangoes'),
        ('honeydew', 'Honeydews'),
    ]

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
    countries = forms.CharField(widget=forms.Select(choices=COUNTRIES))
    terms = forms.BooleanField()

