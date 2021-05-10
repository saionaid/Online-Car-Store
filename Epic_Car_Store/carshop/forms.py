from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'name',
        'type',
        'year_released',
        'description',
        'price',
        'manufacturer',
        'carimg',
        ]



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    location = forms.CharField()



class Meta:
    model = User
    fields = ["username", "email", "location", "password1", "password2"]



class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)



