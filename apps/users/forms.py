from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from helpers.choices import CategoryTypeChoices


class UserForm(UserCreationForm):
    phone = PhoneNumberField()
    category = forms.ChoiceField(choices=CategoryTypeChoices.choices, label='Choice field')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username',
                  'category', 'password1', 'password2')

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        # }


class UserUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'phone', 'photo')
