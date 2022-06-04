from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    count = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    is_admin = forms.BooleanField()