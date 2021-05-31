from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class MakePostForm(forms.Form):
    image = forms.ImageField(label='Image Upload')
    text = forms.CharField(label='Caption', widget=forms.Textarea, empty_value="", required=False)
