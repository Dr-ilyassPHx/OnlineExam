from .models import Student,StudyMentor
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'password', 'name', 'email', 'phone']
        widgets = {'password': forms.PasswordInput()}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_qs = Student.objects.filter(email=email)
        if user_qs.exists():
            raise forms.ValidationError('This Email has already been exist')
        return email


class RegisterFormMentor(forms.ModelForm):
    class Meta:
        model = StudyMentor
        fields = ['user', 'password', 'FirstName','LastName', 'email', 'phone']
        widgets = {'password': forms.PasswordInput()}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_qs = StudyMentor.objects.filter(email=email)
        if user_qs.exists():
            raise forms.ValidationError('This Email is already used')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "phone", "email", "password", "image", "stream", "address"]
