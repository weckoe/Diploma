from django.contrib.auth import get_user_model
from django import forms

user = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ('username',)

    def clean_password2(self):
        # if User.objects.get(username=self.cleaned_data['username']):
        #     raise forms.ValidationError('This username already exists.')
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return self.cleaned_data['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

