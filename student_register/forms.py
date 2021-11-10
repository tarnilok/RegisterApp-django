from django import forms
from .models import StudentInfo

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
        widgets = {
            'photo' : forms.TextInput(attrs={'placeholder' : 'Url'})
        }
 