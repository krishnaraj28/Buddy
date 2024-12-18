from django import forms
from .models import CustomUser,Profile,Event,Resource,Appointment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustomDateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.HiddenInput(), initial='user') 

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'birth_date']
        widgets = {
        'birth_date': CustomDateInput(),
    }
    '''def clean(self):
        if self.birth_date > timezone.now().date():
            raise ValidationError("Birth date cannot be in the future")'''
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password2')
    
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        # Set role to 'user' by default
        self.instance.role = 'user'
        return super().save(commit=commit)


class LoginForm(forms.Form):
    model = CustomUser
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'image']    

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time','location']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),

        }  

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'category']

class ResourceFilterForm(forms.Form):
    category = forms.ChoiceField(label='Category', choices=Resource.CATEGORIES)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','slot', 'message']
        widgets = {
        'date': CustomDateInput(),
    }
    