from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget= forms.TextInput(attrs={'id':"email-address", 'name':"email", 'type':"text", 'autocomplete':"email", 'class':"appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm", 'placeholder':"user name"}))
    password = forms.CharField(required=True, widget= forms.PasswordInput(attrs={'id':"password", 'name':"password", 'type':"password", 'autocomplete':"current-password", 'class':"appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm", 'placeholder':"Password"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        print(f"{username} - {password}")
        try:
            user = models.User.objects.get(username=username)
            print("try here")
            if user.check_password(password):
                print("password check")
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
            
            
        except models.User.DoesNotExist:
            print("User is no valid")
            self.add_error("username", forms.ValidationError("User does not exist"))