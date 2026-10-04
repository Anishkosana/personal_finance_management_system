from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm password"
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user
    
    def clean(self):
         cleaned_data = super().clean()

         password = cleaned_data.get("password")
         password2 = cleaned_data.get("password2")

         if password != password2:
            raise forms.ValidationError("Passwords do not match.")

         return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)